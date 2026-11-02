import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import SVC

from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler


# =========================================================
# PYTHON
# =========================================================

def mean_normal(ns):

    result = ns["calculate_mean"](
        [1, 2, 3, 4, 5]
    )

    assert abs(result - 3.0) < 1e-9


def mean_negative(ns):

    result = ns["calculate_mean"](
        [-5, 5]
    )

    assert abs(result - 0.0) < 1e-9


def mean_single(ns):

    result = ns["calculate_mean"](
        [7]
    )

    assert abs(result - 7.0) < 1e-9


def sum_even_mixed(ns):

    result = ns["sum_even"](
        [1, 2, 3, 4, 5, 6]
    )

    assert result == 12


def sum_even_odd(ns):

    result = ns["sum_even"](
        [1, 3, 5]
    )

    assert result == 0


def sum_even_negative(ns):

    result = ns["sum_even"](
        [-4, -3, -2, 1]
    )

    assert result == -6


# =========================================================
# NUMPY
# =========================================================

def numpy_array(ns):

    assert np.array_equal(
        ns["arr"],
        np.array([10, 20, 30, 40])
    )


def numpy_mean(ns):

    assert abs(
        float(ns["mean"]) - 25.0
    ) < 1e-9


# =========================================================
# PANDAS
# =========================================================

def pandas_age(ns):

    assert (
        ns["df"]["age"].tolist()
        == [18, 20, 22]
    )


def pandas_columns(ns):

    assert list(
        ns["df"].columns
    ) == ["name", "age"]


def pandas_median(ns):

    values = ns["df"]["Age"].tolist()

    assert values == [
        20,
        25,
        30,
        25
    ]


def pandas_no_missing(ns):

    assert not ns[
        "df"
    ]["Age"].isna().any()


# =========================================================
# LINEAR REGRESSION
# =========================================================

def linear_model_type(ns):

    model = ns["model"]

    assert isinstance(
        model,
        LinearRegression
    )


def linear_model_fitted(ns):

    model = ns["model"]

    assert hasattr(
        model,
        "coef_"
    )


def linear_prediction(ns):

    prediction = float(
        ns["model"].predict(
            [[4]]
        )[0]
    )

    assert abs(
        prediction - 8.0
    ) < 1e-6


# =========================================================
# LOGISTIC REGRESSION
# =========================================================

def logistic_type(ns):

    assert isinstance(
        ns["model"],
        LogisticRegression
    )


def logistic_fitted(ns):

    assert hasattr(
        ns["model"],
        "coef_"
    )


def logistic_prediction(ns):

    prediction = ns[
        "model"
    ].predict(
        ns["X_test"]
    )

    assert prediction.shape == (
        ns["y_test"].shape
    )


# =========================================================
# DECISION TREE
# =========================================================

def tree_type(ns):

    assert isinstance(
        ns["model"],
        DecisionTreeClassifier
    )


def tree_fitted(ns):

    assert hasattr(
        ns["model"],
        "tree_"
    )


def tree_prediction(ns):

    prediction = ns[
        "model"
    ].predict(
        ns["X_test"]
    )

    assert len(prediction) == len(
        ns["y_test"]
    )


# =========================================================
# RANDOM FOREST
# =========================================================

def rf_type(ns):

    assert isinstance(
        ns["model"],
        RandomForestClassifier
    )


def rf_estimators(ns):

    assert (
        ns["model"].n_estimators
        == 100
    )


def rf_fitted(ns):

    assert len(
        ns["model"].estimators_
    ) == 100


# =========================================================
# KNN
# =========================================================

def knn_type(ns):

    assert isinstance(
        ns["model"],
        KNeighborsClassifier
    )


def knn_neighbors(ns):

    assert (
        ns["model"].n_neighbors
        == 5
    )


def knn_fitted(ns):

    assert hasattr(
        ns["model"],
        "_fit_X"
    )


# =========================================================
# SVM
# =========================================================

def svm_type(ns):

    assert isinstance(
        ns["model"],
        SVC
    )


def svm_kernel(ns):

    assert (
        ns["model"].kernel
        == "linear"
    )


def svm_fitted(ns):

    assert hasattr(
        ns["model"],
        "support_"
    )


# =========================================================
# K-MEANS
# =========================================================

def kmeans_type(ns):

    assert isinstance(
        ns["model"],
        KMeans
    )


def kmeans_clusters(ns):

    assert (
        ns["model"].n_clusters
        == 3
    )


def kmeans_fitted(ns):

    assert hasattr(
        ns["model"],
        "cluster_centers_"
    )


# =========================================================
# METRICS
# =========================================================

def accuracy_value(ns):

    assert abs(
        float(ns["accuracy"]) - 0.75
    ) < 1e-9


# =========================================================
# PREPROCESSING
# =========================================================

def scaler_type(ns):

    assert isinstance(
        ns["scaler"],
        StandardScaler
    )


def scaler_shape(ns):

    assert (
        ns["X_scaled"].shape
        == ns["X_train"].shape
    )


def scaler_mean(ns):

    assert np.allclose(
        ns["X_scaled"].mean(axis=0),
        0,
        atol=1e-7
    )


# =========================================================
# QUESTION TEST REGISTRY
# =========================================================

TEST_CASES = {

    "python-basic-001": {
        "tests": {
            "Mean with normal values":
                mean_normal,

            "Mean with negative values":
                mean_negative,

            "Mean with one value":
                mean_single,
        }
    },

    "python-medium-001": {
        "tests": {
            "Sum even mixed":
                sum_even_mixed,

            "All odd numbers":
                sum_even_odd,

            "Negative values":
                sum_even_negative,
        }
    },

    "numpy-basic-001": {
        "tests": {
            "Array values":
                numpy_array,

            "Array mean":
                numpy_mean,
        }
    },

    "pandas-basic-001": {
        "tests": {
            "Age values":
                pandas_age,

            "DataFrame columns":
                pandas_columns,
        }
    },

    "pandas-medium-001": {
        "tests": {
            "Median imputation":
                pandas_median,

            "No missing values":
                pandas_no_missing,
        }
    },

    "linear-basic-001": {
        "tests": {
            "Model type":
                linear_model_type,

            "Model fitted":
                linear_model_fitted,

            "Prediction":
                linear_prediction,
        }
    },

    "logistic-basic-001": {
        "tests": {
            "Model type":
                logistic_type,

            "Model fitted":
                logistic_fitted,

            "Prediction shape":
                logistic_prediction,
        }
    },

    "tree-basic-001": {
        "tests": {
            "Model type":
                tree_type,

            "Model fitted":
                tree_fitted,

            "Prediction length":
                tree_prediction,
        }
    },

    "rf-basic-001": {
        "tests": {
            "Model type":
                rf_type,

            "100 estimators":
                rf_estimators,

            "Forest fitted":
                rf_fitted,
        }
    },

    "knn-basic-001": {
        "tests": {
            "Model type":
                knn_type,

            "5 neighbors":
                knn_neighbors,

            "Model fitted":
                knn_fitted,
        }
    },

    "svm-basic-001": {
        "tests": {
            "Model type":
                svm_type,

            "Linear kernel":
                svm_kernel,

            "Model fitted":
                svm_fitted,
        }
    },

    "kmeans-basic-001": {
        "tests": {
            "Model type":
                kmeans_type,

            "3 clusters":
                kmeans_clusters,

            "Model fitted":
                kmeans_fitted,
        }
    },

    "metrics-basic-001": {
        "tests": {
            "Accuracy":
                accuracy_value,
        }
    },

    "preprocess-basic-001": {
        "tests": {
            "Scaler type":
                scaler_type,

            "Scaled shape":
                scaler_shape,

            "Scaled mean":
                scaler_mean,
        }
    },
}


# =========================================================
# HIDDEN SETUP DATA
# =========================================================

def build_setup(question_id):

    setups = {

        "numpy-basic-001": """
import numpy as np

arr = np.array([
    10,
    20,
    30,
    40
])

mean = np.mean(arr)
""",

        "pandas-basic-001": """
import pandas as pd

df = pd.DataFrame({
    "name": [
        "A",
        "B",
        "C"
    ],

    "age": [
        18,
        20,
        22
    ]
})
""",

        "pandas-medium-001": """
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Age": [
        20,
        np.nan,
        30,
        25
    ]
})
""",

        "linear-basic-001": """
from sklearn.linear_model import LinearRegression

X_train = [
    [1],
    [2],
    [3]
]

y_train = [
    2,
    4,
    6
]
""",

        "logistic-basic-001": """
from sklearn.linear_model import LogisticRegression

X_train = [
    [0],
    [1],
    [2],
    [3]
]

y_train = [
    0,
    0,
    1,
    1
]

X_test = [
    [1],
    [2]
]

y_test = [0, 1]
""",

        "tree-basic-001": """
from sklearn.tree import DecisionTreeClassifier

X_train = [
    [0],
    [1],
    [2],
    [3]
]

y_train = [
    0,
    0,
    1,
    1
]

X_test = [
    [1],
    [2]
]

y_test = [0, 1]
""",

        "rf-basic-001": """
from sklearn.ensemble import RandomForestClassifier

X_train = [
    [0],
    [1],
    [2],
    [3]
]

y_train = [
    0,
    0,
    1,
    1
]
""",

        "knn-basic-001": """
from sklearn.neighbors import KNeighborsClassifier

X_train = [
    [0],
    [1],
    [2],
    [3],
    [4],
    [5]
]

y_train = [
    0,
    0,
    0,
    1,
    1,
    1
]
""",

        "svm-basic-001": """
from sklearn.svm import SVC

X_train = [
    [0],
    [1],
    [2],
    [3]
]

y_train = [
    0,
    0,
    1,
    1
]
""",

        "kmeans-basic-001": """
from sklearn.cluster import KMeans

X_train = [
    [0],
    [1],
    [10],
    [11],
    [20],
    [21]
]
""",

        "metrics-basic-001": """
y_test = [
    0,
    1,
    1,
    0
]

y_pred = [
    0,
    1,
    0,
    0
]

accuracy = 0.75
""",

        "preprocess-basic-001": """
import numpy as np

X_train = np.array([
    [1.0, 10.0],
    [2.0, 20.0],
    [3.0, 30.0]
])
"""
    }

    return setups.get(
        question_id,
        ""
    )

# Curated challenges are registered after the original test registry.
def curated_normalize_basic(ns):
    import numpy as np
    original = [2,4,6]
    result = ns["normalize_vector"](original)
    assert np.allclose(result, [0,0.5,1]) and original == [2,4,6]

def curated_normalize_constant(ns):
    import numpy as np
    assert np.allclose(ns["normalize_vector"]([9,9,9]), [0,0,0])

def curated_normalize_negative(ns):
    import numpy as np
    assert np.allclose(ns["normalize_vector"]([-3,-1,1]), [0,.5,1])

def curated_group_basic(ns):
    import pandas as pd
    df = pd.DataFrame({"Department":["A","A","A","B","B"],"Salary":[10.,None,30.,4.,None]})
    original = df.copy(deep=True)
    result=ns["fill_group_median"](df)
    assert result["Salary"].tolist()==[10.,20.,30.,4.,4.]
    assert df.equals(original)

def curated_group_fallback(ns):
    import pandas as pd
    df=pd.DataFrame({"Department":["A","A","B","B"],"Salary":[10.,30.,None,None]})
    r=ns["fill_group_median"](df)
    assert r["Salary"].tolist()==[10.,30.,20.,20.]

def curated_pipeline_structure(ns):
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import StandardScaler,OneHotEncoder
    p=ns["build_preprocessor"](["age"],["city"])
    assert isinstance(p,ColumnTransformer)
    transformers=[x[1] for x in p.transformers]
    assert any(isinstance(x,Pipeline) and any(isinstance(z,StandardScaler) for z in x.steps and [v for _,v in x.steps]) for x in transformers)
    assert any(isinstance(x,Pipeline) and any(isinstance(z,OneHotEncoder) and z.handle_unknown=="ignore" for _,z in x.steps) for x in transformers)

def curated_pipeline_unseen(ns):
    import pandas as pd
    import numpy as np
    p=ns["build_preprocessor"](["age"],["city"])
    train=pd.DataFrame({"age":[10.,20.,None],"city":["A","B","A"],"ignore":[1,2,3]})
    p.fit(train)
    out=p.transform(pd.DataFrame({"age":[None,30.],"city":["Z","A"],"ignore":[6,7]}))
    arr=out.toarray() if hasattr(out,"toarray") else np.asarray(out)
    assert arr.shape==(2,3) and np.isfinite(arr).all()

def curated_histogram(ns):
    from matplotlib.figure import Figure
    fig=ns["make_histogram"]([1,2,2,3],bins=3)
    assert isinstance(fig,Figure) and len(fig.axes)==1
    ax=fig.axes[0]
    assert len(ax.patches)==3 and ax.get_xlabel()=="Value" and ax.get_ylabel()=="Frequency" and ax.get_title()=="Value Distribution"

def curated_heatmap(ns):
    import pandas as pd
    from matplotlib.figure import Figure
    fig=ns["draw_correlation"](pd.DataFrame({"a":[1,2,3],"b":[3,2,1],"label":["a","b","c"]}))
    assert isinstance(fig,Figure) and len(fig.axes)>=1
    assert len(fig.axes[0].collections)>0

TEST_CASES.update({
 "curated-numpy-001":{"tests":{"Normal values":curated_normalize_basic,"Constant input":curated_normalize_constant,"Negative values":curated_normalize_negative}},
 "curated-pandas-001":{"tests":{"Department medians":curated_group_basic,"All-missing group fallback":curated_group_fallback}},
 "curated-sklearn-001":{"tests":{"Pipeline components":curated_pipeline_structure,"Unseen categories":curated_pipeline_unseen}},
 "curated-matplotlib-001":{"tests":{"Histogram structure":curated_histogram}},
 "curated-seaborn-001":{"tests":{"Heatmap created":curated_heatmap}},
})


# Verified public-case diagnostics. Each row corresponds to an existing
# assertion above. Only the first two tests are public; later tests are hidden.
# In particular: do not add private test inputs to this registry.
PUBLIC_CASE_DETAILS = {
    "python-basic-001": {
        "Mean with normal values": {"function": "calculate_mean", "args": [[1, 2, 3, 4, 5]], "input": "numbers = [1, 2, 3, 4, 5]", "expected": 3.0},
        "Mean with negative values": {"function": "calculate_mean", "args": [[-5, 5]], "input": "numbers = [-5, 5]", "expected": 0.0},
    },
    "python-medium-001": {
        "Sum even mixed": {"function": "sum_even", "args": [[1, 2, 3, 4, 5, 6]], "input": "numbers = [1, 2, 3, 4, 5, 6]", "expected": 12},
        "All odd numbers": {"function": "sum_even", "args": [[1, 3, 5]], "input": "numbers = [1, 3, 5]", "expected": 0},
    },
    "numpy-basic-001": {
        "Array values": {"variable": "arr", "input": "arr (NumPy array)", "expected": [10, 20, 30, 40]},
        "Array mean": {"variable": "mean", "input": "mean = np.mean(arr)", "expected": 25.0},
    },
    "metrics-basic-001": {
        "Accuracy": {"variable": "accuracy", "input": "accuracy", "expected": 0.75},
    },
}


# MODELMIND_V4_GENERATED_TESTS
# Deterministic, verified test suites for two Python problems.

import math as _v4_math
import random as _v4_random

PUBLIC_TEST_COUNT = {
    "python-basic-001": 6,
    "python-medium-001": 6,
}

def _v4_mean_case(values):
    frozen = tuple(values)
    expected = _v4_math.fsum(frozen) / len(frozen)

    def check(ns):
        numbers = list(frozen)
        original = numbers.copy()
        actual = ns["calculate_mean"](numbers)

        assert not isinstance(actual, bool)
        assert _v4_math.isfinite(float(actual))
        assert _v4_math.isclose(
            float(actual),
            expected,
            rel_tol=1e-9,
            abs_tol=1e-9,
        ), "Incorrect mean"

        assert numbers == original, "Input list was modified"

    return check


def _v4_even_case(values):
    frozen = tuple(values)
    expected = sum(x for x in frozen if x % 2 == 0)

    def check(ns):
        numbers = list(frozen)
        original = numbers.copy()
        actual = ns["sum_even"](numbers)

        assert type(actual) is int, "Return an integer"
        assert actual == expected, "Incorrect even sum"
        assert numbers == original, "Input list was modified"

    return check


def _v4_public(qid, name, values, function, expected, factory):
    TEST_CASES[qid]["tests"][name] = factory(values)
    PUBLIC_CASE_DETAILS[qid][name] = {
        "function": function,
        "args": [list(values)],
        "input": "numbers = " + repr(list(values)),
        "expected": expected,
    }


# Four more public cases for Calculate Mean.
for name, values in [
    ("Mean with one value", [7]),
    ("Mean with decimals", [0.5, 1.5, 2.5]),
    ("Mean with zeros", [0, 0, 0, 0]),
    ("Mean with mixed signs", [-10, -5, 5, 10]),
]:
    _v4_public(
        "python-basic-001",
        name,
        values,
        "calculate_mean",
        _v4_math.fsum(values) / len(values),
        _v4_mean_case,
    )


# Four more public cases for Sum Even Numbers.
for name, values in [
    ("Negative values", [-4, -3, -2, 1]),
    ("Empty list", []),
    ("Only even numbers", [2, 4, 6, 8]),
    ("Zeros and negative numbers", [0, 0, -8, -3, 7]),
]:
    _v4_public(
        "python-medium-001",
        name,
        values,
        "sum_even",
        sum(x for x in values if x % 2 == 0),
        _v4_even_case,
    )


# Put the six public cases first in the test registry.
for qid in PUBLIC_TEST_COUNT:
    original_tests = TEST_CASES[qid]["tests"]
    public_tests = {
        name: original_tests[name]
        for name in PUBLIC_CASE_DETAILS[qid]
    }
    public_tests.update(original_tests)
    TEST_CASES[qid]["tests"] = public_tests


# Add 120 deterministic hidden cases to each question.
for qid, factory, seed in [
    ("python-basic-001", _v4_mean_case, 62831),
    ("python-medium-001", _v4_even_case, 77123),
]:
    rng = _v4_random.Random(seed)

    for index in range(120):
        count = rng.choice(
            [1, 2, 3, 4, 8, 16, 32, 64]
            if qid == "python-basic-001"
            else [0, 1, 2, 3, 8, 16, 32, 64]
        )

        if qid == "python-basic-001":
            numbers = [
                rng.randint(-10000, 10000)
                / rng.choice([1, 2, 4, 10])
                for _ in range(count)
            ]
        else:
            numbers = [
                rng.randint(-10000, 10000)
                for _ in range(count)
            ]

        name = "Private {:03d}".format(index + 1)
        TEST_CASES[qid]["tests"][name] = factory(numbers)


for qid, public_count in PUBLIC_TEST_COUNT.items():
    total = len(TEST_CASES[qid]["tests"])
    assert total == 126, (qid, total)
    assert len(PUBLIC_CASE_DETAILS[qid]) == public_count




# MODELMIND_FIRST_EIGHT_VERIFIED

import math as _mm_math
import random as _mm_random

def _mm_check(condition, message="Incorrect result"):
    if not condition:
        raise AssertionError(message)


def _mm_function_case(fn, values, expected, kind):
    frozen = tuple(values)

    def test(ns):
        if fn not in ns:
            raise AssertionError(f"Missing function: {fn}")

        argument = list(frozen)
        actual = ns[fn](argument)

        if kind == "list":
            _mm_check(
                isinstance(actual, list),
                "Return a Python list"
            )
            _mm_check(
                actual == expected,
                f"Expected {expected!r}, got {actual!r}"
            )

        else:
            _mm_check(
                not isinstance(actual, bool),
                "Return a numeric value"
            )
            _mm_check(
                _mm_math.isclose(
                    float(actual),
                    float(expected),
                    rel_tol=1e-9,
                    abs_tol=1e-9
                ),
                "Incorrect population variance"
            )

    return test


def _mm_variable_case(variable, check, message):
    def test(ns):
        _mm_check(variable in ns, f"Missing variable: {variable}")
        _mm_check(check(ns), message)

    return test


def _mm_register(qid, public_cases, hidden_cases):
    TEST_CASES[qid] = {
        "tests": dict(public_cases + hidden_cases)
    }
    PUBLIC_TEST_COUNT[qid] = len(public_cases)


def _mm_public(qid, name, test, input_text,
               expected, variable=None, function=None,
               args=None):
    spec = {
        "input": input_text,
        "expected": expected,
    }

    if variable is not None:
        spec["variable"] = variable

    if function is not None:
        spec["function"] = function
        spec["args"] = args

    PUBLIC_CASE_DETAILS.setdefault(qid, {})[name] = spec

    return name, test


# =========================================================
# 1. REMOVE NEGATIVE NUMBERS
# =========================================================

qid = "python-advanced-001"
public = []

for name, numbers in [
    ("Consecutive negatives", [-3, -2, -1, 5]),
    ("Mixed numbers", [4, -1, 0, -2, 7]),
    ("All negative", [-5, -4, -3]),
    ("No negatives", [0, 1, 2, 3]),
    ("Empty list", []),
    ("Repeated values", [-2, -2, 2, -2, 2]),
]:
    expected = [x for x in numbers if x >= 0]

    test = _mm_function_case(
        "remove_negative", numbers, expected, "list"
    )

    public.append(_mm_public(
        qid, name, test,
        f"numbers = {numbers!r}",
        expected,
        function="remove_negative",
        args=[numbers],
    ))

rng = _mm_random.Random(12031)
hidden = []

for i in range(80):
    size = rng.randint(0, 100)
    values = [rng.randint(-100, 100) for _ in range(size)]
    expected = [x for x in values if x >= 0]

    hidden.append((
        f"Private {i + 1:03d}",
        _mm_function_case(
            "remove_negative", values, expected, "list"
        )
    ))

_mm_register(qid, public, hidden)


# =========================================================
# 2. POPULATION VARIANCE
# =========================================================

qid = "statistics-medium-001"
public = []

for name, numbers in [
    ("Consecutive numbers", [1, 2, 3, 4, 5]),
    ("Constant values", [7, 7, 7, 7]),
    ("Negative numbers", [-3, -1, 1, 3]),
    ("Single value", [10]),
    ("Decimal values", [0.5, 1.5, 2.5]),
    ("Repeated values", [2, 2, 4, 4]),
]:
    mean = _mm_math.fsum(numbers) / len(numbers)
    expected = _mm_math.fsum(
        (x - mean) ** 2 for x in numbers
    ) / len(numbers)

    test = _mm_function_case(
        "variance", numbers, expected, "numeric"
    )

    public.append(_mm_public(
        qid, name, test,
        f"values = {numbers!r}",
        expected,
        function="variance",
        args=[numbers],
    ))

rng = _mm_random.Random(22061)
hidden = []

for i in range(80):
    size = rng.randint(1, 50)
    values = [
        rng.randint(-500, 500) / 4
        for _ in range(size)
    ]

    mean = _mm_math.fsum(values) / len(values)
    expected = _mm_math.fsum(
        (x - mean) ** 2 for x in values
    ) / len(values)

    hidden.append((
        f"Private {i + 1:03d}",
        _mm_function_case(
            "variance", values, expected, "numeric"
        )
    ))

_mm_register(qid, public, hidden)


# =========================================================
# 3. NUMPY ARRAY + MEAN
# =========================================================

import numpy as _mm_np
import pandas as _mm_pd

qid = "numpy-basic-001"

array_expected = _mm_np.array([10, 20, 30, 40])

public = [
    _mm_public(
        qid, "Correct array values",
        _mm_variable_case(
            "arr",
            lambda ns: isinstance(ns["arr"], _mm_np.ndarray)
            and _mm_np.array_equal(ns["arr"], array_expected),
            "arr must be the required NumPy array"
        ),
        "arr = np.array([10, 20, 30, 40])",
        [10, 20, 30, 40],
        variable="arr",
    ),
    _mm_public(
        qid, "Correct mean",
        _mm_variable_case(
            "mean",
            lambda ns: _mm_math.isclose(
                float(ns["mean"]), 25.0
            ),
            "Mean must equal 25.0"
        ),
        "arr = [10, 20, 30, 40]",
        25.0,
        variable="mean",
    ),
    _mm_public(
        qid, "Array shape",
        _mm_variable_case(
            "arr",
            lambda ns: getattr(ns["arr"], "shape", None) == (4,),
            "Array must be one-dimensional with four elements"
        ),
        "arr.shape",
        (4,),
        variable="arr",
    ),
    _mm_public(
        qid, "Array size",
        _mm_variable_case(
            "arr",
            lambda ns: getattr(ns["arr"], "size", None) == 4,
            "Array must contain four elements"
        ),
        "arr.size",
        4,
        variable="arr",
    ),
]

hidden = [
    ("Private dtype check", _mm_variable_case(
        "arr",
        lambda ns: _mm_np.issubdtype(
            ns["arr"].dtype, _mm_np.number
        ),
        "Array must contain numeric values"
    )),
    ("Private mean consistency", _mm_variable_case(
        "mean",
        lambda ns: _mm_np.isclose(
            float(ns["mean"]), _mm_np.mean(ns["arr"])
        ),
        "Mean must match the array"
    )),
]

_mm_register(qid, public, hidden)


# =========================================================
# 4. NUMPY MIN-MAX NORMALIZATION
# =========================================================

qid = "numpy-medium-001"
expected_normalized = _mm_np.array([0, 1/3, 2/3, 1])

checks = [
    ("Normalized values",
     lambda ns: _mm_np.allclose(
         ns["normalized"], expected_normalized
     )),
    ("Minimum equals zero",
     lambda ns: _mm_np.isclose(
         _mm_np.min(ns["normalized"]), 0
     )),
    ("Maximum equals one",
     lambda ns: _mm_np.isclose(
         _mm_np.max(ns["normalized"]), 1
     )),
    ("Correct output shape",
     lambda ns: _mm_np.shape(ns["normalized"]) == (4,)),
]

public = []

for name, condition in checks:
    public.append(_mm_public(
        qid, name,
        _mm_variable_case(
            "normalized", condition,
            "Incorrect min-max normalization"
        ),
        "arr = np.array([10, 20, 30, 40])",
        expected_normalized.tolist(),
        variable="normalized",
    ))

hidden = [
    ("Private finite check", _mm_variable_case(
        "normalized",
        lambda ns: _mm_np.isfinite(ns["normalized"]).all(),
        "Output must be finite"
    )),
]

_mm_register(qid, public, hidden)


# =========================================================
# 5. NUMPY COLUMN STANDARDIZATION
# =========================================================

qid = "numpy-advanced-001"

expected_x = _mm_np.array([
    [1.0, 10.0],
    [2.0, 20.0],
    [3.0, 30.0]
])
expected_scaled = (
    expected_x - expected_x.mean(axis=0)
) / expected_x.std(axis=0)

checks = [
    ("Standardized values",
     lambda ns: _mm_np.allclose(
         ns["X_scaled"], expected_scaled
     )),
    ("Column means",
     lambda ns: _mm_np.allclose(
         _mm_np.mean(ns["X_scaled"], axis=0), 0
     )),
    ("Column standard deviations",
     lambda ns: _mm_np.allclose(
         _mm_np.std(ns["X_scaled"], axis=0), 1
     )),
    ("Correct matrix shape",
     lambda ns: _mm_np.shape(ns["X_scaled"]) == (3, 2)),
]

public = []

for name, condition in checks:
    public.append(_mm_public(
        qid, name,
        _mm_variable_case(
            "X_scaled", condition,
            "Incorrect column standardization"
        ),
        "X = [[1, 10], [2, 20], [3, 30]]",
        expected_scaled.tolist(),
        variable="X_scaled",
    ))

_mm_register(qid, public, [
    ("Private finite check", _mm_variable_case(
        "X_scaled",
        lambda ns: _mm_np.isfinite(ns["X_scaled"]).all(),
        "Output must be finite"
    )),
])


# =========================================================
# 6. PANDAS DATAFRAME
# =========================================================

qid = "pandas-basic-001"

expected_df = _mm_pd.DataFrame({
    "name": ["A", "B", "C"],
    "age": [18, 20, 22],
})

checks = [
    ("DataFrame type",
     lambda ns: isinstance(ns["df"], _mm_pd.DataFrame)),
    ("Correct columns",
     lambda ns: list(ns["df"].columns) == ["name", "age"]),
    ("Correct names",
     lambda ns: ns["df"]["name"].tolist() == ["A", "B", "C"]),
    ("Correct ages",
     lambda ns: ns["df"]["age"].tolist() == [18, 20, 22]),
    ("Correct shape",
     lambda ns: ns["df"].shape == (3, 2)),
]

public = []

for name, condition in checks:
    public.append(_mm_public(
        qid, name,
        _mm_variable_case(
            "df", condition,
            "Incorrect DataFrame"
        ),
        "Create names A, B, C with ages 18, 20, 22",
        expected_df.to_string(index=False),
        variable="df",
    ))

_mm_register(qid, public, [
    ("Private complete-data check", _mm_variable_case(
        "df",
        lambda ns: not ns["df"].isna().any().any(),
        "DataFrame must not contain missing values"
    )),
])


# =========================================================
# 7. PANDAS MEDIAN IMPUTATION
# =========================================================

qid = "pandas-medium-001"
expected_age = [20, 25, 30, 25]

checks = [
    ("Age values after imputation",
     lambda ns: ns["df"]["Age"].tolist() == expected_age),
    ("No missing Age values",
     lambda ns: not ns["df"]["Age"].isna().any()),
    ("Age median",
     lambda ns: ns["df"]["Age"].median() == 25),
    ("Correct row count",
     lambda ns: len(ns["df"]) == 4),
]

public = []

for name, condition in checks:
    public.append(_mm_public(
        qid, name,
        _mm_variable_case(
            "df", condition,
            "Incorrect median imputation"
        ),
        "Age = [20, NaN, 30, 25]",
        expected_age,
        variable="df",
    ))

_mm_register(qid, public, [
    ("Private numeric check", _mm_variable_case(
        "df",
        lambda ns: _mm_pd.api.types.is_numeric_dtype(
            ns["df"]["Age"]
        ),
        "Age must remain numeric"
    )),
])


# =========================================================
# 8. PANDAS GROUP AND AGGREGATE
# =========================================================

qid = "pandas-advanced-001"
expected_groups = {"A": 15.0, "B": 40.0}

def _mm_group_result(ns):
    result = ns["result"]

    if isinstance(result, _mm_pd.DataFrame):
        if "Department" in result.columns:
            result = result.set_index("Department")

        if "Salary" in result.columns:
            result = result["Salary"]

    if isinstance(result, _mm_pd.Series):
        return result.to_dict()

    return dict(result)


checks = [
    ("Correct department averages",
     lambda ns: _mm_group_result(ns) == expected_groups),
    ("Both departments present",
     lambda ns: set(_mm_group_result(ns)) == {"A", "B"}),
    ("Department A average",
     lambda ns: _mm_group_result(ns)["A"] == 15),
    ("Department B average",
     lambda ns: _mm_group_result(ns)["B"] == 40),
]

public = []

for name, condition in checks:
    public.append(_mm_public(
        qid, name,
        _mm_variable_case(
            "result", condition,
            "Incorrect department aggregation"
        ),
        "A: [10,20]; B: [30,50]",
        expected_groups,
        variable="result",
    ))

_mm_register(qid, public, [
    ("Private numeric averages", _mm_variable_case(
        "result",
        lambda ns: all(
            isinstance(x, (int, float, _mm_np.number))
            for x in _mm_group_result(ns).values()
        ),
        "Group averages must be numeric"
    )),
])

# ============================================================
# MODELMIND REGRESSION TEST PACK V1
# Questions:
# linear-basic-001
# linear-medium-001
# poly-medium-001
# ============================================================

import numpy as _reg_np
from sklearn.linear_model import LinearRegression as _RegLinear
from sklearn.preprocessing import PolynomialFeatures as _RegPoly
from sklearn.utils.validation import check_is_fitted as _reg_is_fitted


def _reg_get_model(ns):
    model = ns.get("model")

    assert isinstance(model, _RegLinear), (
        "Expected a LinearRegression model."
    )

    _reg_is_fitted(model)
    return model


def _reg_linear_test(values):
    values = _reg_np.asarray(values, dtype=float).reshape(-1, 1)
    expected = 2.0 * values.ravel()

    def check(ns):
        model = _reg_get_model(ns)
        actual = model.predict(values)

        assert _reg_np.allclose(
            actual, expected, rtol=1e-6, atol=1e-6
        ), "Linear regression predictions are incorrect."

    return check


def _reg_prediction_test(ns):
    model = _reg_get_model(ns)

    assert "prediction" in ns, (
        "Missing prediction variable."
    )

    expected = 8.0
    actual = _reg_np.asarray(ns["prediction"]).reshape(-1)

    assert actual.size == 1, (
        "prediction must contain exactly one value."
    )

    assert _reg_np.isclose(
        float(actual[0]), expected, atol=1e-6
    ), "Expected prediction approximately 8.0."


def _reg_poly_model(ns):
    poly = ns.get("poly")
    model = ns.get("model")

    assert isinstance(poly, _RegPoly), (
        "poly must be a PolynomialFeatures instance."
    )
    assert poly.degree == 2, (
        "PolynomialFeatures degree must equal 2."
    )

    assert isinstance(model, _RegLinear), (
        "model must be a LinearRegression instance."
    )

    _reg_is_fitted(poly)
    _reg_is_fitted(model)

    return poly, model


def _reg_poly_predict(values):
    values = _reg_np.asarray(
        values, dtype=float
    ).reshape(-1, 1)

    def check(ns):
        poly, model = _reg_poly_model(ns)

        transformed = poly.transform(values)
        actual = model.predict(transformed)
        expected = values.ravel() ** 2

        assert _reg_np.allclose(
            actual,
            expected,
            rtol=1e-5,
            atol=1e-5
        ), "Polynomial predictions are incorrect."

    return check


def _reg_register(qid, public, hidden):
    existing = TEST_CASES.get(qid, {}).get("tests", {})

    # Preserve existing tests and their order.
    combined = dict(existing)

    for name, test in public:
        if name in combined:
            raise ValueError(
                f"Duplicate regression test: {qid} / {name}"
            )
        combined[name] = test

    public_count = len(combined)

    for name, test in hidden:
        if name in combined:
            raise ValueError(
                f"Duplicate regression test: {qid} / {name}"
            )
        combined[name] = test

    TEST_CASES[qid] = {"tests": combined}
    PUBLIC_TEST_COUNT[qid] = public_count


# -----------------------------
# BASIC: FIT LINEAR REGRESSION
# -----------------------------

_reg_register(
    "linear-basic-001",
    public=[
        (
            "New prediction x=4",
            _reg_linear_test([4])
        ),
        (
            "New prediction x=5",
            _reg_linear_test([5])
        ),
        (
            "Zero and negative inputs",
            _reg_linear_test([0, -1, -3])
        ),
    ],
    hidden=[
        (
            f"Regression hidden {i + 1}",
            _reg_linear_test([i + 6, -(i + 2)])
        )
        for i in range(12)
    ]
)


# -----------------------------
# MEDIUM: PREDICT REGRESSION
# -----------------------------

_reg_register(
    "linear-medium-001",
    public=[
        ("Prediction variable", _reg_prediction_test),
        ("Predict x=0", _reg_linear_test([0])),
        ("Predict x=5", _reg_linear_test([5])),
        ("Predict negative values", _reg_linear_test([-1, -4])),
    ],
    hidden=[
        (
            f"Prediction hidden {i + 1}",
            _reg_linear_test([i + 7, -(i + 1)])
        )
        for i in range(12)
    ]
)


# --------------------------------
# MEDIUM: DEGREE-2 POLYNOMIAL MODEL
# --------------------------------

_reg_register(
    "poly-medium-001",
    public=[
        ("Polynomial model configuration",
         lambda ns: _reg_poly_model(ns)),
        ("Prediction at x=4", _reg_poly_predict([4])),
        ("Prediction at x=5", _reg_poly_predict([5])),
        ("Prediction at x=0", _reg_poly_predict([0])),
        ("Predictions for negative x",
         _reg_poly_predict([-2, -3])),
    ],
    hidden=[
        (
            f"Polynomial hidden {i + 1}",
            _reg_poly_predict([i + 6, -(i + 1)])
        )
        for i in range(12)
    ]
)


