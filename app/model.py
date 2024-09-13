from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_model():
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, stratify=iris.target, random_state=42
    )

    rf = RandomForestClassifier(
        n_estimators=10, max_depth=2, oob_score=True, random_state=42
    )
    rf.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, rf.predict(X_test))
    return rf, accuracy


def predict(model, input_data):
    return model.predict(input_data)
