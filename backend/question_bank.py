from typing import Any


# =========================================================
# QUESTION BANK
# =========================================================

QUESTIONS = [

    # =====================================================
    # PYTHON
    # =====================================================

    {
        "id": "python-basic-001",
        "topic": "Python",
        "level": "Basic",
        "type": "Coding",
        "title": "Calculate the mean",
        "question": (
            "Write a function calculate_mean(numbers) that "
            "returns the arithmetic mean of a list."
        ),
        "starterCode": (
            "def calculate_mean(numbers):\n"
            "    # Write your solution\n"
            "    pass\n"
        ),
        "evaluatorId": "python-basic-001",
        "tags": ["functions", "lists", "arithmetic"],
    },

    {
        "id": "python-medium-001",
        "topic": "Python",
        "level": "Medium",
        "type": "Coding",
        "title": "Sum even numbers",
        "question": (
            "Write sum_even(numbers) that returns the sum "
            "of all even numbers."
        ),
        "starterCode": (
            "def sum_even(numbers):\n"
            "    # Write your solution\n"
            "    pass\n"
        ),
        "evaluatorId": "python-medium-001",
        "tags": ["loops", "conditions", "lists"],
    },

    {
        "id": "python-advanced-001",
        "topic": "Python",
        "level": "Advanced",
        "type": "Debugging",
        "title": "Fix list mutation",
        "question": (
            "The function below is intended to remove all "
            "negative values. Fix the implementation."
        ),
        "starterCode": (
            "def remove_negative(numbers):\n"
            "    for x in numbers:\n"
            "        if x < 0:\n"
            "            numbers.remove(x)\n"
            "    return numbers\n"
        ),
        "evaluatorId": "python-advanced-001",
        "tags": ["lists", "mutation", "debugging"],
    },


    # =====================================================
    # NUMPY
    # =====================================================

    {
        "id": "numpy-basic-001",
        "topic": "NumPy",
        "level": "Basic",
        "type": "Coding",
        "title": "Create an array and calculate its mean",
        "question": (
            "Create a NumPy array containing 10, 20, 30, 40 "
            "and calculate its mean."
        ),
        "starterCode": (
            "import numpy as np\n\n"
            "arr = None\n"
            "mean = None\n"
        ),
        "evaluatorId": "numpy-basic-001",
        "tags": ["numpy", "array", "mean"],
    },

    {
        "id": "numpy-medium-001",
        "topic": "NumPy",
        "level": "Medium",
        "type": "Coding",
        "title": "Normalize an array",
        "question": (
            "Normalize the array using min-max normalization:\n"
            "(x - min) / (max - min)"
        ),
        "starterCode": (
            "import numpy as np\n\n"
            "arr = np.array([10, 20, 30, 40])\n"
            "# Create normalized\n"
            "normalized = None\n"
        ),
        "evaluatorId": "numpy-medium-001",
        "tags": ["numpy", "normalization"],
    },

    {
        "id": "numpy-advanced-001",
        "topic": "NumPy",
        "level": "Advanced",
        "type": "Coding",
        "title": "Standardize columns",
        "question": (
            "Standardize each column of X so that each column "
            "has mean approximately 0 and standard deviation 1."
        ),
        "starterCode": (
            "import numpy as np\n\n"
            "X = np.array([\n"
            "    [1.0, 10.0],\n"
            "    [2.0, 20.0],\n"
            "    [3.0, 30.0]\n"
            "])\n\n"
            "X_scaled = None\n"
        ),
        "evaluatorId": "numpy-advanced-001",
        "tags": ["numpy", "standardization", "scaling"],
    },


    # =====================================================
    # PANDAS
    # =====================================================

    {
        "id": "pandas-basic-001",
        "topic": "Pandas",
        "level": "Basic",
        "type": "Coding",
        "title": "Create a DataFrame",
        "question": (
            "Create a DataFrame containing names A, B, C "
            "and ages 18, 20, 22."
        ),
        "starterCode": (
            "import pandas as pd\n\n"
            "df = None\n"
        ),
        "evaluatorId": "pandas-basic-001",
        "tags": ["pandas", "dataframe"],
    },

    {
        "id": "pandas-medium-001",
        "topic": "Pandas",
        "level": "Medium",
        "type": "Coding",
        "title": "Median imputation",
        "question": (
            "Fill the missing Age value using the median "
            "of the Age column."
        ),
        "starterCode": (
            "import pandas as pd\n"
            "import numpy as np\n\n"
            "df = pd.DataFrame({\n"
            "    'Age': [20, np.nan, 30, 25]\n"
            "})\n\n"
            "# Complete the preprocessing\n"
        ),
        "evaluatorId": "pandas-medium-001",
        "tags": ["pandas", "missing-values", "imputation"],
    },

    {
        "id": "pandas-advanced-001",
        "topic": "Pandas",
        "level": "Advanced",
        "type": "Coding",
        "title": "Group and aggregate",
        "question": (
            "Given a DataFrame containing department and salary, "
            "calculate the average salary for every department."
        ),
        "starterCode": (
            "import pandas as pd\n\n"
            "df = pd.DataFrame({\n"
            "    'Department': ['A', 'A', 'B', 'B'],\n"
            "    'Salary': [10, 20, 30, 50]\n"
            "})\n\n"
            "result = None\n"
        ),
        "evaluatorId": "pandas-advanced-001",
        "tags": ["groupby", "aggregation", "pandas"],
    },


    # =====================================================
    # STATISTICS
    # =====================================================

    {
        "id": "statistics-basic-001",
        "topic": "Statistics",
        "level": "Basic",
        "type": "Mathematics",
        "title": "Mean",
        "question": (
            "Calculate the mean of 4, 6, 8, 10."
        ),
        "options": [
            "6",
            "7",
            "8",
            "9",
        ],
        "correctOption": 1,
        "explanation": (
            "Mean = (4 + 6 + 8 + 10) / 4 = 7."
        ),
        "tags": ["mean", "statistics"],
    },

    {
        "id": "statistics-medium-001",
        "topic": "Statistics",
        "level": "Medium",
        "type": "Coding",
        "title": "Calculate variance",
        "question": (
            "Write a function variance(values) that calculates "
            "population variance."
        ),
        "starterCode": (
            "def variance(values):\n"
            "    # Write your solution\n"
            "    pass\n"
        ),
        "evaluatorId": "statistics-medium-001",
        "tags": ["variance", "statistics", "python"],
    },

    {
        "id": "statistics-advanced-001",
        "topic": "Statistics",
        "level": "Advanced",
        "type": "Mathematics",
        "title": "Standard deviation reasoning",
        "question": (
            "If every value in a dataset is multiplied by 3, "
            "what happens to its standard deviation?"
        ),
        "options": [
            "It stays the same",
            "It becomes 3 times larger",
            "It becomes 9 times larger",
            "It becomes 1/3 as large",
        ],
        "correctOption": 1,
        "explanation": (
            "Standard deviation scales by the absolute value "
            "of the multiplication factor."
        ),
        "tags": ["standard-deviation", "scaling"],
    },


    # =====================================================
    # PREPROCESSING
    # =====================================================

    {
        "id": "preprocess-basic-001",
        "topic": "Preprocessing",
        "level": "Basic",
        "type": "Coding",
        "title": "StandardScaler",
        "question": (
            "Use StandardScaler to standardize X_train."
        ),
        "starterCode": (
            "import numpy as np\n"
            "from sklearn.preprocessing import StandardScaler\n\n"
            "X_train = np.array([\n"
            "    [1.0, 10.0],\n"
            "    [2.0, 20.0],\n"
            "    [3.0, 30.0]\n"
            "])\n\n"
            "scaler = None\n"
            "X_scaled = None\n"
        ),
        "evaluatorId": "preprocess-basic-001",
        "tags": ["standardization", "sklearn"],
    },

    {
        "id": "preprocess-medium-001",
        "topic": "Preprocessing",
        "level": "Medium",
        "type": "Debugging",
        "title": "Prevent data leakage",
        "question": (
            "Fix the preprocessing pipeline so that the scaler "
            "is fitted only on training data."
        ),
        "starterCode": (
            "scaler.fit(X_test)\n"
            "X_train_scaled = scaler.transform(X_train)\n"
            "X_test_scaled = scaler.transform(X_test)\n"
        ),
        "evaluatorId": "preprocess-medium-001",
        "tags": ["data-leakage", "scaling", "validation"],
    },

    {
        "id": "preprocess-advanced-001",
        "topic": "Preprocessing",
        "level": "Advanced",
        "type": "Coding",
        "title": "Build a preprocessing pipeline",
        "question": (
            "Build a Pipeline containing StandardScaler followed "
            "by LogisticRegression."
        ),
        "starterCode": (
            "from sklearn.pipeline import Pipeline\n"
            "from sklearn.preprocessing import StandardScaler\n"
            "from sklearn.linear_model import LogisticRegression\n\n"
            "model = None\n"
        ),
        "evaluatorId": "preprocess-advanced-001",
        "tags": ["pipeline", "scaling", "logistic-regression"],
    },


    # =====================================================
    # FEATURE ENGINEERING
    # =====================================================

    {
        "id": "feature-basic-001",
        "topic": "Feature Engineering",
        "level": "Basic",
        "type": "Concept",
        "title": "Why create features?",
        "question": (
            "What is the main purpose of feature engineering?"
        ),
        "options": [
            "Always increase dataset size",
            "Create more useful representations for a model",
            "Remove the target column",
            "Guarantee 100% accuracy",
        ],
        "correctOption": 1,
        "explanation": (
            "Feature engineering transforms raw data into "
            "representations that can help the model learn."
        ),
        "tags": ["features", "representation"],
    },

    {
        "id": "feature-medium-001",
        "topic": "Feature Engineering",
        "level": "Medium",
        "type": "Coding",
        "title": "Create BMI",
        "question": (
            "Create a BMI column using weight_kg / height_m^2."
        ),
        "starterCode": (
            "df['BMI'] = None\n"
        ),
        "evaluatorId": "feature-medium-001",
        "tags": ["feature-engineering", "pandas"],
    },

    {
        "id": "feature-advanced-001",
        "topic": "Feature Engineering",
        "level": "Advanced",
        "type": "Coding",
        "title": "One-hot encode a categorical feature",
        "question": (
            "Convert the categorical City column into one-hot "
            "encoded features."
        ),
        "starterCode": (
            "from sklearn.preprocessing import OneHotEncoder\n\n"
            "encoder = None\n"
            "encoded = None\n"
        ),
        "evaluatorId": "feature-advanced-001",
        "tags": ["one-hot", "categorical", "encoding"],
    },


    # =====================================================
    # METRICS
    # =====================================================

    {
        "id": "metrics-basic-001",
        "topic": "Metrics",
        "level": "Basic",
        "type": "Coding",
        "title": "Calculate accuracy",
        "question": (
            "Calculate classification accuracy from y_test and y_pred."
        ),
        "starterCode": (
            "from sklearn.metrics import accuracy_score\n\n"
            "y_test = [0, 1, 1, 0]\n"
            "y_pred = [0, 1, 0, 0]\n\n"
            "accuracy = None\n"
        ),
        "evaluatorId": "metrics-basic-001",
        "tags": ["accuracy", "classification"],
    },

    {
        "id": "metrics-medium-001",
        "topic": "Metrics",
        "level": "Medium",
        "type": "Coding",
        "title": "Calculate F1 score",
        "question": (
            "Calculate the F1 score for the supplied predictions."
        ),
        "starterCode": (
            "from sklearn.metrics import f1_score\n\n"
            "y_test = [0, 1, 1, 0]\n"
            "y_pred = [0, 1, 0, 0]\n\n"
            "f1 = None\n"
        ),
        "evaluatorId": "metrics-medium-001",
        "tags": ["f1", "precision", "recall"],
    },

    {
        "id": "metrics-advanced-001",
        "topic": "Metrics",
        "level": "Advanced",
        "type": "Model / Algorithm",
        "title": "Choose the right metric",
        "question": (
            "A fraud detection system has extremely rare fraud "
            "cases. Missing a fraud case is much more expensive "
            "than investigating a false alarm. Which metric should "
            "receive strong attention?"
        ),
        "options": [
            "Recall",
            "R-squared",
            "MAE",
            "Silhouette score",
        ],
        "correctOption": 0,
        "explanation": (
            "Recall measures how many actual positive cases "
            "are successfully detected."
        ),
        "tags": ["fraud", "recall", "classification"],
    },


    # =====================================================
    # LINEAR REGRESSION
    # =====================================================

    {
        "id": "linear-basic-001",
        "topic": "Linear Regression",
        "level": "Basic",
        "type": "Coding",
        "title": "Fit Linear Regression",
        "question": (
            "Fit LinearRegression on X_train and y_train."
        ),
        "starterCode": (
            "from sklearn.linear_model import LinearRegression\n\n"
            "X_train = [[1], [2], [3]]\n"
            "y_train = [2, 4, 6]\n\n"
            "model = None\n"
        ),
        "evaluatorId": "linear-basic-001",
        "tags": ["regression", "sklearn"],
    },

    {
        "id": "linear-medium-001",
        "topic": "Linear Regression",
        "level": "Medium",
        "type": "Coding",
        "title": "Predict with regression",
        "question": (
            "Train the model and predict the target for x = 4."
        ),
        "starterCode": (
            "from sklearn.linear_model import LinearRegression\n\n"
            "X_train = [[1], [2], [3]]\n"
            "y_train = [2, 4, 6]\n\n"
            "model = LinearRegression()\n"
            "# Complete training and prediction\n"
            "prediction = None\n"
        ),
        "evaluatorId": "linear-medium-001",
        "tags": ["fit", "predict", "regression"],
    },

    {
        "id": "linear-advanced-001",
        "topic": "Linear Regression",
        "level": "Advanced",
        "type": "Model / Algorithm",
        "title": "Underfitting reasoning",
        "question": (
            "A linear model has very poor training performance "
            "and poor test performance. What is the most likely issue?"
        ),
        "options": [
            "High variance",
            "Underfitting",
            "Data leakage",
            "Perfect generalization",
        ],
        "correctOption": 1,
        "explanation": (
            "Poor performance on both training and test data "
            "often indicates high bias or underfitting."
        ),
        "tags": ["bias", "underfitting"],
    },


    # =====================================================
    # POLYNOMIAL REGRESSION
    # =====================================================

    {
        "id": "poly-basic-001",
        "topic": "Polynomial Regression",
        "level": "Basic",
        "type": "Concept",
        "title": "Polynomial features",
        "question": (
            "What does PolynomialFeatures allow a linear model to do?"
        ),
        "options": [
            "Create polynomial feature terms",
            "Automatically collect more rows",
            "Delete outliers",
            "Perform clustering",
        ],
        "correctOption": 0,
        "explanation": (
            "PolynomialFeatures creates terms such as x², x³ "
            "and interaction terms."
        ),
        "tags": ["polynomial", "features"],
    },

    {
        "id": "poly-medium-001",
        "topic": "Polynomial Regression",
        "level": "Medium",
        "type": "Coding",
        "title": "Build degree-2 regression",
        "question": (
            "Use PolynomialFeatures with degree 2 and fit "
            "LinearRegression."
        ),
        "starterCode": (
            "from sklearn.preprocessing import PolynomialFeatures\n"
            "from sklearn.linear_model import LinearRegression\n\n"
            "X = [[1], [2], [3]]\n"
            "y = [1, 4, 9]\n\n"
            "poly = None\n"
            "model = None\n"
        ),
        "evaluatorId": "poly-medium-001",
        "tags": ["polynomial", "degree", "regression"],
    },

    {
        "id": "poly-advanced-001",
        "topic": "Polynomial Regression",
        "level": "Advanced",
        "type": "Coding",
        "title": "Control overfitting",
        "question": (
            "Build a degree-5 polynomial model with Ridge "
            "regularization."
        ),
        "starterCode": (
            "from sklearn.preprocessing import PolynomialFeatures\n"
            "from sklearn.linear_model import Ridge\n\n"
            "poly = None\n"
            "model = None\n"
        ),
        "evaluatorId": "poly-advanced-001",
        "tags": ["overfitting", "ridge", "polynomial"],
    },


    # =====================================================
    # LOGISTIC REGRESSION
    # =====================================================

    {
        "id": "logistic-basic-001",
        "topic": "Logistic Regression",
        "level": "Basic",
        "type": "Coding",
        "title": "Fit Logistic Regression",
        "question": (
            "Fit LogisticRegression on the provided training data."
        ),
        "starterCode": (
            "from sklearn.linear_model import LogisticRegression\n\n"
            "X_train = [[0], [1], [2], [3]]\n"
            "y_train = [0, 0, 1, 1]\n\n"
            "model = None\n"
        ),
        "evaluatorId": "logistic-basic-001",
        "tags": ["classification", "logistic-regression"],
    },

    {
        "id": "logistic-medium-001",
        "topic": "Logistic Regression",
        "level": "Medium",
        "type": "Coding",
        "title": "Predict probabilities",
        "question": (
            "Train LogisticRegression and generate class probabilities."
        ),
        "starterCode": (
            "from sklearn.linear_model import LogisticRegression\n\n"
            "X_train = [[0], [1], [2], [3]]\n"
            "y_train = [0, 0, 1, 1]\n"
            "X_test = [[1], [2]]\n\n"
            "model = LogisticRegression()\n"
            "probabilities = None\n"
        ),
        "evaluatorId": "logistic-medium-001",
        "tags": ["predict_proba", "classification"],
    },

    {
        "id": "logistic-advanced-001",
        "topic": "Logistic Regression",
        "level": "Advanced",
        "type": "Model / Algorithm",
        "title": "Threshold reasoning",
        "question": (
            "If false negatives are much more expensive than "
            "false positives, what is a reasonable threshold strategy?"
        ),
        "options": [
            "Always increase the threshold",
            "Consider lowering the threshold",
            "Always use threshold 1.0",
            "Threshold does not affect predictions",
        ],
        "correctOption": 1,
        "explanation": (
            "Lowering the threshold can increase positive predictions "
            "and potentially improve recall."
        ),
        "tags": ["threshold", "recall", "false-negative"],
    },


    # =====================================================
    # GRADIENT DESCENT
    # =====================================================

    {
        "id": "gradient-basic-001",
        "topic": "Gradient Descent",
        "level": "Basic",
        "type": "Mathematics",
        "title": "Gradient update",
        "question": (
            "If w = 2, learning rate = 0.1 and gradient = 4, "
            "what is the next value of w?"
        ),
        "options": [
            "1.6",
            "2.4",
            "0.4",
            "6",
        ],
        "correctOption": 0,
        "explanation": (
            "w_new = w - learning_rate * gradient = "
            "2 - 0.1 * 4 = 1.6."
        ),
        "tags": ["gradient-descent", "learning-rate"],
    },

    {
        "id": "gradient-medium-001",
        "topic": "Gradient Descent",
        "level": "Medium",
        "type": "Coding",
        "title": "Perform one gradient step",
        "question": (
            "Implement one gradient descent update for w."
        ),
        "starterCode": (
            "w = 2.0\n"
            "learning_rate = 0.1\n"
            "gradient = 4.0\n\n"
            "# Calculate new_w\n"
            "new_w = None\n"
        ),
        "evaluatorId": "gradient-medium-001",
        "tags": ["gradient", "optimization"],
    },

    {
        "id": "gradient-advanced-001",
        "topic": "Gradient Descent",
        "level": "Advanced",
        "type": "Coding",
        "title": "Implement iterative updates",
        "question": (
            "Implement gradient descent for a simple quadratic "
            "function until the parameter approaches the minimum."
        ),
        "starterCode": (
            "def optimize(w, learning_rate, steps):\n"
            "    # Complete the optimization\n"
            "    pass\n"
        ),
        "evaluatorId": "gradient-advanced-001",
        "tags": ["optimization", "iterations", "gradient"],
    },


    # =====================================================
    # CROSS VALIDATION
    # =====================================================

    {
        "id": "cv-basic-001",
        "topic": "Cross Validation",
        "level": "Basic",
        "type": "Concept",
        "title": "Purpose of cross validation",
        "question": (
            "Why is cross-validation used?"
        ),
        "options": [
            "To estimate generalization more reliably",
            "To guarantee zero error",
            "To increase the number of labels",
            "To remove the target",
        ],
        "correctOption": 0,
        "explanation": (
            "Cross-validation evaluates a model across multiple "
            "train/validation splits."
        ),
        "tags": ["cross-validation", "generalization"],
    },

    {
        "id": "cv-medium-001",
        "topic": "Cross Validation",
        "level": "Medium",
        "type": "Coding",
        "title": "Run cross validation",
        "question": (
            "Use cross_val_score with 5 folds."
        ),
        "starterCode": (
            "from sklearn.model_selection import cross_val_score\n"
            "from sklearn.linear_model import LogisticRegression\n\n"
            "model = LogisticRegression()\n"
            "scores = None\n"
        ),
        "evaluatorId": "cv-medium-001",
        "tags": ["cross-validation", "k-fold"],
    },

    {
        "id": "cv-advanced-001",
        "topic": "Cross Validation",
        "level": "Advanced",
        "type": "Coding",
        "title": "Prevent preprocessing leakage",
        "question": (
            "Combine preprocessing and a model in a Pipeline "
            "before cross-validation."
        ),
        "starterCode": (
            "from sklearn.pipeline import Pipeline\n"
            "from sklearn.preprocessing import StandardScaler\n"
            "from sklearn.linear_model import LogisticRegression\n\n"
            "pipeline = None\n"
        ),
        "evaluatorId": "cv-advanced-001",
        "tags": ["pipeline", "cross-validation", "leakage"],
    },


    # =====================================================
    # HYPERPARAMETER TUNING
    # =====================================================

    {
        "id": "tuning-basic-001",
        "topic": "Hyperparameter Tuning",
        "level": "Basic",
        "type": "Concept",
        "title": "Hyperparameter",
        "question": (
            "Which of the following is a hyperparameter?"
        ),
        "options": [
            "A learned model coefficient",
            "Number of neighbors in KNN",
            "A prediction",
            "A test label",
        ],
        "correctOption": 1,
        "explanation": (
            "n_neighbors is selected before training and is therefore "
            "a hyperparameter."
        ),
        "tags": ["hyperparameter", "knn"],
    },

    {
        "id": "tuning-medium-001",
        "topic": "Hyperparameter Tuning",
        "level": "Medium",
        "type": "Coding",
        "title": "GridSearchCV",
        "question": (
            "Use GridSearchCV to search over n_neighbors."
        ),
        "starterCode": (
            "from sklearn.model_selection import GridSearchCV\n"
            "from sklearn.neighbors import KNeighborsClassifier\n\n"
            "model = KNeighborsClassifier()\n"
            "param_grid = {'n_neighbors': [3, 5, 7]}\n\n"
            "search = None\n"
        ),
        "evaluatorId": "tuning-medium-001",
        "tags": ["grid-search", "knn"],
    },

    {
        "id": "tuning-advanced-001",
        "topic": "Hyperparameter Tuning",
        "level": "Advanced",
        "type": "Model / Algorithm",
        "title": "Avoid tuning on the test set",
        "question": (
            "Why should the final test set not be used to choose "
            "the best hyperparameters?"
        ),
        "options": [
            "It can cause optimistic performance estimates",
            "It makes the model nonlinear",
            "It removes all features",
            "It prevents model training",
        ],
        "correctOption": 0,
        "explanation": (
            "Using the test set for model selection leaks information "
            "from the final evaluation set."
        ),
        "tags": ["test-set", "leakage", "tuning"],
    },


    # =====================================================
    # KNN
    # =====================================================

    {
        "id": "knn-basic-001",
        "topic": "KNN",
        "level": "Basic",
        "type": "Coding",
        "title": "Train KNN",
        "question": (
            "Create KNeighborsClassifier with n_neighbors=5 "
            "and fit it."
        ),
        "starterCode": (
            "from sklearn.neighbors import KNeighborsClassifier\n\n"
            "model = None\n"
        ),
        "evaluatorId": "knn-basic-001",
        "tags": ["knn", "classification"],
    },

    {
        "id": "knn-medium-001",
        "topic": "KNN",
        "level": "Medium",
        "type": "Coding",
        "title": "Predict with KNN",
        "question": (
            "Train KNN and generate predictions for X_test."
        ),
        "starterCode": (
            "from sklearn.neighbors import KNeighborsClassifier\n\n"
            "model = KNeighborsClassifier(n_neighbors=5)\n"
            "# Fit and predict\n"
            "predictions = None\n"
        ),
        "evaluatorId": "knn-medium-001",
        "tags": ["knn", "prediction"],
    },

    {
        "id": "knn-advanced-001",
        "topic": "KNN",
        "level": "Advanced",
        "type": "Model / Algorithm",
        "title": "Why scaling matters",
        "question": (
            "Why is feature scaling especially important for KNN?"
        ),
        "options": [
            "KNN uses distance calculations",
            "KNN always performs regression",
            "KNN ignores features",
            "KNN cannot classify",
        ],
        "correctOption": 0,
        "explanation": (
            "Distance-based algorithms can be dominated by features "
            "with larger numerical scales."
        ),
        "tags": ["distance", "scaling", "knn"],
    },


    # =====================================================
    # NAIVE BAYES
    # =====================================================

    {
        "id": "nb-basic-001",
        "topic": "Naive Bayes",
        "level": "Basic",
        "type": "Concept",
        "title": "Naive assumption",
        "question": (
            "What simplifying assumption does Naive Bayes make?"
        ),
        "options": [
            "Features are conditionally independent given the class",
            "All features must be identical",
            "There are no classes",
            "The target must be continuous",
        ],
        "correctOption": 0,
        "explanation": (
            "Naive Bayes assumes conditional independence of features "
            "given the class."
        ),
        "tags": ["naive-bayes", "probability"],
    },

    {
        "id": "nb-medium-001",
        "topic": "Naive Bayes",
        "level": "Medium",
        "type": "Coding",
        "title": "Train Gaussian Naive Bayes",
        "question": (
            "Create GaussianNB and fit it on the supplied data."
        ),
        "starterCode": (
            "from sklearn.naive_bayes import GaussianNB\n\n"
            "model = None\n"
        ),
        "evaluatorId": "nb-medium-001",
        "tags": ["naive-bayes", "gaussian"],
    },

    {
        "id": "nb-advanced-001",
        "topic": "Naive Bayes",
        "level": "Advanced",
        "type": "Model / Algorithm",
        "title": "Text classification choice",
        "question": (
            "Why can Naive Bayes be a strong baseline for text "
            "classification?"
        ),
        "options": [
            "It works well with high-dimensional sparse features",
            "It requires 3D images",
            "It cannot handle many features",
            "It only works with regression",
        ],
        "correctOption": 0,
        "explanation": (
            "Naive Bayes is often computationally efficient and "
            "works well with sparse high-dimensional representations."
        ),
        "tags": ["text", "sparse", "classification"],
    },


    # =====================================================
    # DECISION TREE
    # =====================================================

    {
        "id": "tree-basic-001",
        "topic": "Decision Tree",
        "level": "Basic",
        "type": "Coding",
        "title": "Train a decision tree",
        "question": (
            "Create DecisionTreeClassifier and fit it."
        ),
        "starterCode": (
            "from sklearn.tree import DecisionTreeClassifier\n\n"
            "model = None\n"
        ),
        "evaluatorId": "tree-basic-001",
        "tags": ["decision-tree", "classification"],
    },

    {
        "id": "tree-medium-001",
        "topic": "Decision Tree",
        "level": "Medium",
        "type": "Debugging",
        "title": "Control tree depth",
        "question": (
            "A decision tree is heavily overfitting. Modify the "
            "model so its maximum depth is 3."
        ),
        "starterCode": (
            "from sklearn.tree import DecisionTreeClassifier\n\n"
            "model = DecisionTreeClassifier()\n"
        ),
        "evaluatorId": "tree-medium-001",
        "tags": ["tree", "overfitting", "max-depth"],
    },

    {
        "id": "tree-advanced-001",
        "topic": "Decision Tree",
        "level": "Advanced",
        "type": "Coding",
        "title": "Tune a decision tree",
        "question": (
            "Create a DecisionTreeClassifier using "
            "min_samples_leaf=5 and max_depth=4."
        ),
        "starterCode": (
            "from sklearn.tree import DecisionTreeClassifier\n\n"
            "model = None\n"
        ),
        "evaluatorId": "tree-advanced-001",
        "tags": ["tree", "regularization", "tuning"],
    },


    # =====================================================
    # RANDOM FOREST
    # =====================================================

    {
        "id": "rf-basic-001",
        "topic": "Random Forest",
        "level": "Basic",
        "type": "Coding",
        "title": "Train Random Forest",
        "question": (
            "Create RandomForestClassifier with 100 estimators."
        ),
        "starterCode": (
            "from sklearn.ensemble import RandomForestClassifier\n\n"
            "model = None\n"
        ),
        "evaluatorId": "rf-basic-001",
        "tags": ["random-forest", "ensemble"],
    },

    {
        "id": "rf-medium-001",
        "topic": "Random Forest",
        "level": "Medium",
        "type": "Coding",
        "title": "Random Forest prediction",
        "question": (
            "Fit RandomForestClassifier and generate predictions."
        ),
        "starterCode": (
            "from sklearn.ensemble import RandomForestClassifier\n\n"
            "model = RandomForestClassifier(n_estimators=100)\n"
            "predictions = None\n"
        ),
        "evaluatorId": "rf-medium-001",
        "tags": ["random-forest", "prediction"],
    },

    {
        "id": "rf-advanced-001",
        "topic": "Random Forest",
        "level": "Advanced",
        "type": "Model / Algorithm",
        "title": "Why Random Forest reduces variance",
        "question": (
            "Why can Random Forest generalize better than a single "
            "deep decision tree?"
        ),
        "options": [
            "It averages many diverse trees",
            "It always uses only one feature",
            "It removes all training data",
            "It never creates trees",
        ],
        "correctOption": 0,
        "explanation": (
            "Averaging diverse trees reduces variance compared "
            "with relying on one highly variable tree."
        ),
        "tags": ["variance", "ensemble", "bagging"],
    },


    # =====================================================
    # SVM
    # =====================================================

    {
        "id": "svm-basic-001",
        "topic": "SVM",
        "level": "Basic",
        "type": "Coding",
        "title": "Linear SVM",
        "question": (
            "Create SVC with a linear kernel and fit it."
        ),
        "starterCode": (
            "from sklearn.svm import SVC\n\n"
            "model = None\n"
        ),
        "evaluatorId": "svm-basic-001",
        "tags": ["svm", "linear-kernel"],
    },

    {
        "id": "svm-medium-001",
        "topic": "SVM",
        "level": "Medium",
        "type": "Debugging",
        "title": "Choose a kernel",
        "question": (
            "Modify the model to use an RBF kernel."
        ),
        "starterCode": (
            "from sklearn.svm import SVC\n\n"
            "model = SVC(kernel='linear')\n"
        ),
        "evaluatorId": "svm-medium-001",
        "tags": ["svm", "rbf", "kernel"],
    },

    {
        "id": "svm-advanced-001",
        "topic": "SVM",
        "level": "Advanced",
        "type": "Coding",
        "title": "Train an RBF SVM",
        "question": (
            "Create an SVC using kernel='rbf' and C=2."
        ),
        "starterCode": (
            "from sklearn.svm import SVC\n\n"
            "model = None\n"
        ),
        "evaluatorId": "svm-advanced-001",
        "tags": ["svm", "rbf", "c"],
    },


    # =====================================================
    # K-MEANS
    # =====================================================

    {
        "id": "kmeans-basic-001",
        "topic": "K-Means",
        "level": "Basic",
        "type": "Coding",
        "title": "Create K-Means",
        "question": (
            "Create KMeans with 3 clusters and fit it."
        ),
        "starterCode": (
            "from sklearn.cluster import KMeans\n\n"
            "model = None\n"
        ),
        "evaluatorId": "kmeans-basic-001",
        "tags": ["clustering", "kmeans"],
    },

    {
        "id": "kmeans-medium-001",
        "topic": "K-Means",
        "level": "Medium",
        "type": "Coding",
        "title": "Generate cluster labels",
        "question": (
            "Fit KMeans with 3 clusters and generate labels."
        ),
        "starterCode": (
            "from sklearn.cluster import KMeans\n\n"
            "model = KMeans(n_clusters=3, random_state=42)\n"
            "labels = None\n"
        ),
        "evaluatorId": "kmeans-medium-001",
        "tags": ["clustering", "labels"],
    },

    {
        "id": "kmeans-advanced-001",
        "topic": "K-Means",
        "level": "Advanced",
        "type": "Model / Algorithm",
        "title": "Choosing K",
        "question": (
            "Which technique is commonly used to help choose "
            "a suitable K for K-Means?"
        ),
        "options": [
            "Elbow method",
            "Confusion matrix",
            "ROC curve only",
            "Accuracy on labels that do not exist",
        ],
        "correctOption": 0,
        "explanation": (
            "The elbow method examines how clustering error changes "
            "as K increases."
        ),
        "tags": ["kmeans", "elbow"],
    },


    # =====================================================
    # PCA
    # =====================================================

    {
        "id": "pca-basic-001",
        "topic": "PCA",
        "level": "Basic",
        "type": "Concept",
        "title": "Purpose of PCA",
        "question": (
            "What is a common use of PCA?"
        ),
        "options": [
            "Dimensionality reduction",
            "Adding labels",
            "Creating target values",
            "Guaranteeing accuracy",
        ],
        "correctOption": 0,
        "explanation": (
            "PCA projects data into a lower-dimensional space "
            "while preserving as much variance as possible."
        ),
        "tags": ["pca", "dimensionality-reduction"],
    },

    {
        "id": "pca-medium-001",
        "topic": "PCA",
        "level": "Medium",
        "type": "Coding",
        "title": "Reduce to two components",
        "question": (
            "Apply PCA with n_components=2."
        ),
        "starterCode": (
            "from sklearn.decomposition import PCA\n\n"
            "pca = None\n"
            "X_reduced = None\n"
        ),
        "evaluatorId": "pca-medium-001",
        "tags": ["pca", "components"],
    },

    {
        "id": "pca-advanced-001",
        "topic": "PCA",
        "level": "Advanced",
        "type": "Real-world ML",
        "title": "PCA before visualization",
        "question": (
            "You have 100-dimensional data and want to visualize "
            "it in 2D. Why might PCA be useful?"
        ),
        "options": [
            "It can create a lower-dimensional representation",
            "It creates labels automatically",
            "It guarantees perfect separation",
            "It converts regression into classification",
        ],
        "correctOption": 0,
        "explanation": (
            "PCA can project high-dimensional data into a lower-dimensional "
            "space suitable for visualization."
        ),
        "tags": ["pca", "visualization"],
    },


    # =====================================================
    # ADABOOST / GRADIENT BOOSTING
    # =====================================================

    {
        "id": "boost-basic-001",
        "topic": "AdaBoost / Gradient Boosting",
        "level": "Basic",
        "type": "Concept",
        "title": "Boosting idea",
        "question": (
            "What is the main idea behind boosting?"
        ),
        "options": [
            "Combine sequential weak learners to build a stronger model",
            "Train only one random model",
            "Remove all weak learners",
            "Use no training data",
        ],
        "correctOption": 0,
        "explanation": (
            "Boosting builds an ensemble by combining weak learners "
            "sequentially."
        ),
        "tags": ["boosting", "ensemble"],
    },

    {
        "id": "boost-medium-001",
        "topic": "AdaBoost / Gradient Boosting",
        "level": "Medium",
        "type": "Coding",
        "title": "Train AdaBoost",
        "question": (
            "Create AdaBoostClassifier with 50 estimators and fit it."
        ),
        "starterCode": (
            "from sklearn.ensemble import AdaBoostClassifier\n\n"
            "model = None\n"
        ),
        "evaluatorId": "boost-medium-001",
        "tags": ["adaboost", "ensemble"],
    },

    {
        "id": "boost-advanced-001",
        "topic": "AdaBoost / Gradient Boosting",
        "level": "Advanced",
        "type": "Coding",
        "title": "Gradient boosting classifier",
        "question": (
            "Create GradientBoostingClassifier with "
            "n_estimators=100 and fit it."
        ),
        "starterCode": (
            "from sklearn.ensemble import GradientBoostingClassifier\n\n"
            "model = None\n"
        ),
        "evaluatorId": "boost-advanced-001",
        "tags": ["gradient-boosting", "ensemble"],
    },


    # =====================================================
    # XGBOOST
    # =====================================================

    {
        "id": "xgb-basic-001",
        "topic": "XGBoost",
        "level": "Basic",
        "type": "Concept",
        "title": "Why XGBoost is popular",
        "question": (
            "Which description best matches XGBoost?"
        ),
        "options": [
            "A gradient boosting framework with regularization and efficient implementations",
            "A clustering-only algorithm",
            "A dimensionality reduction algorithm",
            "A database engine",
        ],
        "correctOption": 0,
        "explanation": (
            "XGBoost is a gradient boosting framework designed "
            "for strong predictive performance and efficiency."
        ),
        "tags": ["xgboost", "boosting"],
    },

    {
        "id": "xgb-medium-001",
        "topic": "XGBoost",
        "level": "Medium",
        "type": "Model / Algorithm",
        "title": "Boosting versus bagging",
        "question": (
            "Which statement best describes a key difference?"
        ),
        "options": [
            "Boosting builds learners sequentially; bagging can build them independently",
            "Bagging always uses gradient descent",
            "Boosting cannot use trees",
            "They are exactly the same",
        ],
        "correctOption": 0,
        "explanation": (
            "Boosting typically trains learners sequentially, while "
            "bagging trains learners independently and aggregates them."
        ),
        "tags": ["boosting", "bagging", "ensemble"],
    },

    {
        "id": "xgb-advanced-001",
        "topic": "XGBoost",
        "level": "Advanced",
        "type": "Real-world ML",
        "title": "Fraud detection model selection",
        "question": (
            "For a fraud detection problem with severe class imbalance, "
            "which approach is more appropriate?"
        ),
        "options": [
            "Evaluate only accuracy",
            "Use imbalance-aware training and evaluate precision/recall-based metrics",
            "Delete all fraud examples",
            "Always predict the majority class",
        ],
        "correctOption": 1,
        "explanation": (
            "Severe imbalance makes accuracy potentially misleading. "
            "The training strategy and evaluation should account for the minority class."
        ),
        "tags": ["fraud", "imbalance", "xgboost"],
    },
]


# =========================================================
# LOOKUP
# =========================================================



# =========================================================
# QUESTION BANK EXPANSION - BATCH 1
# =========================================================
from question_bank_extra_batch1 import ADDITIONAL_QUESTIONS
QUESTIONS.extend(ADDITIONAL_QUESTIONS)


# =========================================================
# QUESTION BANK EXPANSION - BATCH 2
# =========================================================
from question_bank_extra_batch2 import ADDITIONAL_QUESTIONS
QUESTIONS.extend(ADDITIONAL_QUESTIONS)


# =========================================================
# QUESTION BANK EXPANSION - BATCH 3
# =========================================================
from question_bank_extra_batch3 import ADDITIONAL_QUESTIONS as _BATCH3_QUESTIONS

_BATCH3_EXISTING_IDS = {q["id"] for q in QUESTIONS}

QUESTIONS.extend(
    q for q in _BATCH3_QUESTIONS
    if q["id"] not in _BATCH3_EXISTING_IDS
)

del _BATCH3_EXISTING_IDS
del _BATCH3_QUESTIONS

from curated_questions import CURATED
QUESTIONS.extend(CURATED)

QUESTION_MAP = {
    question["id"]: question
    for question in QUESTIONS
}


def get_question(question_id: str):
    return QUESTION_MAP.get(question_id)


def public_question(question: dict[str, Any]) -> dict[str, Any]:
    """
    Never send correctOption or hidden evaluator information
    to the browser.
    """

    result = dict(question)

    for key in ("correctOption", "expectedAnswer", "evaluatorId", "solution", "explanation"):
        result.pop(key, None)

    return result
_MM_NUMERICAL_FIXED = {'statistics-basic-004': {'question': 'Compute the population variance of the eight values [2, 4, 4, 4, 5, 5, 7, 9]. Divide by N, not N-1. Give the exact numerical result.', 'expectedAnswer': 4.0, 'explanation': 'The mean is 5; the squared deviations sum to 32; population variance = 32/8 = 4.'}, 'statistics-medium-002': {'question': 'For sorted data [1, 2, 3, 4, 5, 100], compute IQR = Q3 - Q1 using the median-of-halves convention. Return one number.', 'expectedAnswer': 3.0, 'explanation': 'Lower half [1,2,3] has median 2; upper half [4,5,100] has median 5; IQR = 3.'}, 'statistics-advanced-002': {'question': 'Disease prevalence is 1%; sensitivity is 90%; specificity is 95%. A patient tests positive. Use Bayes theorem to calculate P(disease | positive). Enter a probability between 0 and 1, rounded to six decimals.', 'expectedAnswer': 0.153846, 'explanation': 'P(disease|+) = 0.01*0.90 / (0.01*0.90+0.99*0.05) = 0.153846.'}, 'gradient-basic-004': {'question': 'A gradient-descent update uses w_new = w - learning_rate * gradient. Given w=2, learning_rate=0.1, gradient=4, compute w_new.', 'expectedAnswer': 1.6, 'explanation': '2 - (0.1 * 4) = 1.6.'}, 'stats-advanced-001': {'question': 'Given P(A)=0.4 and P(B|A)=0.5, compute P(A ∩ B). Return one probability.', 'expectedAnswer': 0.2, 'explanation': 'P(A ∩ B) = P(A) * P(B|A) = 0.4 * 0.5 = 0.2.'}, 'stats-advanced-003': {'question': 'A fair six-sided die has outcomes 1, 2, 3, 4, 5, 6. What is the expected value of one roll?', 'expectedAnswer': 3.5, 'explanation': '(1+2+3+4+5+6)/6 = 3.5.'}, 'curated-statistics-001': {'question': 'Compute the population variance of [2, 4, 6, 8] (divide by N=4). Enter one number.', 'expectedAnswer': 5.0, 'explanation': 'Mean 5, squared deviations 9+1+1+9=20; variance = 20/4 = 5.'}}

# MODELMIND_NUMERICAL_QA_BATCH2
for _mm_q in QUESTIONS:
    _mm_patch = _MM_NUMERICAL_FIXED.get(_mm_q.get("id"))
    if _mm_patch is not None:
        _mm_q.update(_mm_patch)
