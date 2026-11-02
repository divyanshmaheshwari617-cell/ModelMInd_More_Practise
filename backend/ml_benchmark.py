"""ModelMind local synthetic benchmark API, v1. Educational prototype, NOT a public secure judge.
Add `from ml_benchmark import router as ml_benchmark_router` and `app.include_router(ml_benchmark_router)` to backend/main.py.
"""
from __future__ import annotations
import csv
import io
from functools import lru_cache
from typing import Literal
import numpy as np
from fastapi import APIRouter, HTTPException, Body
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.svm import SVC, SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix, classification_report, mean_absolute_error, mean_squared_error, r2_score

router = APIRouter(prefix='/api/ml', tags=['ML Synthetic Benchmarks'])

CLASSIFIERS = {
    'logistic-regression': lambda: make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, random_state=42)),
    'decision-tree': lambda: DecisionTreeClassifier(max_depth=6, random_state=42),
    'random-forest': lambda: RandomForestClassifier(n_estimators=80, random_state=42, n_jobs=1),
    'knn': lambda: make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
    'svm': lambda: make_pipeline(StandardScaler(), SVC(random_state=42)),
    'gaussian-nb': lambda: GaussianNB(),
    'gradient-boosting': lambda: GradientBoostingClassifier(random_state=42),
}
REGRESSORS = {
    'linear-regression': lambda: LinearRegression(),
    'ridge': lambda: make_pipeline(StandardScaler(), Ridge(alpha=1.0)),
    'lasso': lambda: make_pipeline(StandardScaler(), Lasso(alpha=0.1, max_iter=10000)),
    'elastic-net': lambda: make_pipeline(StandardScaler(), ElasticNet(alpha=0.1, max_iter=10000)),
    'decision-tree-regressor': lambda: DecisionTreeRegressor(max_depth=6, random_state=42),
    'random-forest-regressor': lambda: RandomForestRegressor(n_estimators=80, random_state=42, n_jobs=1),
    'knn-regressor': lambda: make_pipeline(StandardScaler(), KNeighborsRegressor(n_neighbors=5)),
    'svr': lambda: make_pipeline(StandardScaler(), SVR()),
    'gradient-boosting-regressor': lambda: GradientBoostingRegressor(random_state=42),
}

LEVELS = {
    'basic': {'n_samples': 360, 'n_features': 6, 'noise': 5, 'flip_y': 0, 'class_sep': 1.8},
    'medium': {'n_samples': 600, 'n_features': 10, 'noise': 15, 'flip_y': 0.03, 'class_sep': 1.0},
    'advanced': {'n_samples': 850, 'n_features': 14, 'noise': 30, 'flip_y': 0.07, 'class_sep': 0.7},
}
TARGET_NAME = 'target'


def _catalog():
    return [{'id': f'{name}-{level}', 'model': name, 'level': level, 'task': task, 'targetColumn': TARGET_NAME,
             'targetAvailableIn': 'training data only',
             'instructions': f'Train a {name} model using the supplied training CSV and submit predictions in test-row order.'}
            for task, pool in [('classification', CLASSIFIERS), ('regression', REGRESSORS)]
            for name in pool for level in LEVELS]

CATALOG = {c['id']: c for c in _catalog()}

@lru_cache(maxsize=100)
def _data(challenge_id: str):
    c = CATALOG[challenge_id]
    config = LEVELS[c['level']]
    n = config['n_samples']
    f = config['n_features']
    # Deterministic by challenge ID, but not cryptographically private. Not for competitive leaderboards.
    seed = 101 + sum((i + 1) * ord(ch) for i, ch in enumerate(challenge_id)) % 20000
    if c['task'] == 'classification':
        X, y = make_classification(n_samples=n, n_features=f, n_informative=max(3, f//2),
            n_redundant=1, n_repeated=0, n_classes=2, flip_y=config['flip_y'],
            class_sep=config['class_sep'], weights=[0.6, 0.4], random_state=seed)
    else:
        X, y = make_regression(n_samples=n, n_features=f, n_informative=max(3, f//2),
            noise=config['noise'], random_state=seed)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,
        random_state=seed+7, stratify=y if c['task']=='classification' else None)
    # Reference fitted on the same training split. Test labels are not returned via API.
    ref = (CLASSIFIERS if c['task']=='classification' else REGRESSORS)[c['model']]()
    ref.fit(Xtr, ytr)
    reference_preds = ref.predict(Xte)
    cols = [f'feature_{i+1}' for i in range(f)]
    return Xtr, Xte, ytr, yte, reference_preds, cols


def _metrics(task: str, true: np.ndarray, predictions: np.ndarray):
    if task=='classification':
        labels = sorted(int(v) for v in np.unique(true))
        precision, recall, f1, _ = precision_recall_fscore_support(true, predictions, average='weighted', zero_division=0)
        macro_p, macro_r, macro_f1, _ = precision_recall_fscore_support(true, predictions, average='macro', zero_division=0)
        return {'accuracy': round(float(accuracy_score(true, predictions)), 6),
                'precision_weighted': round(float(precision), 6), 'recall_weighted': round(float(recall), 6),
                'f1_weighted': round(float(f1), 6), 'precision_macro': round(float(macro_p), 6),
                'recall_macro': round(float(macro_r), 6), 'f1_macro': round(float(macro_f1), 6),
                'confusion_matrix': confusion_matrix(true, predictions, labels=labels).tolist(),
                'confusion_labels': labels,
                'per_class': classification_report(true, predictions, labels=labels, output_dict=True, zero_division=0)}
    return {'mae': round(float(mean_absolute_error(true, predictions)), 6),
            'mse': round(float(mean_squared_error(true, predictions)), 6),
            'rmse': round(float(np.sqrt(mean_squared_error(true, predictions))), 6),
            'r2': round(float(r2_score(true, predictions)), 6)}

@router.get('/challenges')
def challenges():
    return list(CATALOG.values())

@router.get('/dataset/{challenge_id}')
def dataset(challenge_id: str):
    if challenge_id not in CATALOG:
        raise HTTPException(404, 'Unknown challenge')
    Xtr, Xte, ytr, _, _, cols = _data(challenge_id)
    return {'challenge': CATALOG[challenge_id], 'featureColumns': cols,
            'targetColumn': TARGET_NAME, 'trainRows': len(Xtr), 'testRows': len(Xte),
            'train': [dict(zip(cols, map(float, x))) | {TARGET_NAME: float(y) if CATALOG[challenge_id]['task']=='regression' else int(y)} for x,y in zip(Xtr,ytr)],
            'test': [dict(zip(cols, map(float, x))) for x in Xte]}

@router.get('/dataset/{challenge_id}/train.csv')
def train_csv(challenge_id: str):
    if challenge_id not in CATALOG:
        raise HTTPException(404, 'Unknown challenge')
    Xtr, _, ytr, _, _, cols = _data(challenge_id)
    f = io.StringIO(newline='')
    w = csv.writer(f)
    w.writerow(cols + [TARGET_NAME])
    w.writerows([*map(float,x), float(y)] for x,y in zip(Xtr,ytr))
    f.seek(0)
    return StreamingResponse(iter([f.getvalue()]), media_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename="{challenge_id}_train.csv"'})

@router.get('/dataset/{challenge_id}/test.csv')
def test_csv(challenge_id: str):
    if challenge_id not in CATALOG:
        raise HTTPException(404, 'Unknown challenge')
    _, Xte, _, _, _, cols = _data(challenge_id)
    f = io.StringIO(newline='')
    w = csv.writer(f)
    w.writerow(['row_id'] + cols)
    for i, x in enumerate(Xte, start=1):
        w.writerow([i] + list(map(float, x)))
    return StreamingResponse(iter([f.getvalue()]), media_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename="{challenge_id}_test.csv"'})


def _parse_prediction_column(content: str) -> list[float]:
    if len(content) > 2_000_000:
        raise HTTPException(422, 'Prediction column is too large')
    try:
        csv_rows = list(csv.reader(io.StringIO(content, newline='')))
    except csv.Error as exc:
        raise HTTPException(422, f'Invalid CSV: {exc}')
    csv_rows = [r for r in csv_rows if any(cell.strip() for cell in r)]
    if not csv_rows:
        raise HTTPException(422, 'Prediction column is empty')
    if any(len(r) != 1 for r in csv_rows):
        raise HTTPException(422, 'Provide exactly ONE prediction column, without row IDs or features')
    entries = [r[0].strip().lstrip('\ufeff') for r in csv_rows]
    if entries[0].lower() in {'prediction', 'predictions', 'y_pred', 'target', 'output'}:
        entries.pop(0)
    if not entries:
        raise HTTPException(422, 'No prediction values after the header')
    if len(entries) > 10000:
        raise HTTPException(422, 'Too many prediction values')
    try:
        values = [float(v) for v in entries]
    except ValueError:
        raise HTTPException(422, 'Every row must contain one numeric prediction (optional header: prediction)')
    return values


@router.post('/evaluate-column')
def evaluate_column(challenge_id: str, content: str = Body(..., media_type='text/plain')):
    return evaluate(EvaluationRequest(challenge_id=challenge_id,
                                      predictions=_parse_prediction_column(content)))


class EvaluationRequest(BaseModel):
    challenge_id: str
    predictions: list[float | int] = Field(min_length=1, max_length=10000)

@router.post('/evaluate')
def evaluate(payload: EvaluationRequest):
    if payload.challenge_id not in CATALOG:
        raise HTTPException(404, 'Unknown challenge')
    c = CATALOG[payload.challenge_id]
    _, Xte, _, yte, ref_preds, _ = _data(payload.challenge_id)
    p = np.asarray(payload.predictions, dtype=float)
    if len(p) != len(Xte):
        raise HTTPException(422, f'Expected {len(Xte)} predictions, received {len(p)}')
    if not np.isfinite(p).all():
        raise HTTPException(422, 'Predictions must be finite')
    if c['task']=='classification':
        if not np.isin(p, [0,1]).all():
            raise HTTPException(422, 'Classification predictions must be class labels 0 or 1, not probabilities')
        p = p.astype(int)
    # Row-level feedback is intentional for local educational practice.
    # It reveals test labels after evaluation; do not reuse for secure hidden exams.
    rows = []
    for i, (actual, student_pred, reference_pred) in enumerate(zip(yte, p, ref_preds), start=1):
        delta = float(student_pred - actual)
        row = {'row': i, 'actual': float(actual), 'predicted': float(student_pred),
               'reference': float(reference_pred)}
        if c['task'] == 'classification':
            row.update({'correct': bool(student_pred == actual),
                        'reference_correct': bool(reference_pred == actual)})
        else:
            row.update({'error': round(delta, 6), 'absolute_error': round(abs(delta), 6)})
        rows.append(row)
    return {'challenge': c, 'n_test': len(Xte),
            'student': _metrics(c['task'], yte, p),
            'reference': _metrics(c['task'], yte, ref_preds),
            'rowComparison': rows,
            'gradingStatus': 'practice benchmark — not an accepted/rejected verdict',
            'privacyNote': 'Row-by-row true labels are shown after submission for learning; this is not a secure hidden-test judge.'}
