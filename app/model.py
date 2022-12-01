from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets
from joblib import dump
from joblib import load
import pandas as pd
from pathlib import Path


def load_tabular_model():
    """
    returns the model, train it first if it does not exist.
    """
    if not Path("model_tabular/iris.joblib").is_file():
        train_and_save_tabular()
    tabular_model = load(pathlib.Path("model_tabular/iris.joblib"))
    return tabular_model


def train_and_save_tabular():
    """
    Trains a simple classifier on a tabular 3-classes dataset (iris).
    """

    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    X_train, X_test, y_train, y_test = train_test_split(
        df[iris.feature_names],
        iris.target,
        test_size=0.2,
        stratify=iris.target,
        random_state=42,
    )

    print("Training model")

    rf = RandomForestClassifier(
        n_estimators=10, max_depth=2, oob_score=True, random_state=42
    )
    rf.fit(X_train, y_train)

    predicted = rf.predict(X_test)
    accuracy = accuracy_score(y_test, predicted)
    print(f"Out-of-bag score estimate: {rf.oob_score_:.3}")
    print(f"Mean accuracy score: {accuracy:.3}")

    print("Saving model")
    dump(rf, Path("model_tabular/iris.joblib"))
