import numpy as np
from model import predict, train_model
from persistence import load_model, save_model


def get_or_train_model():
    try:
        model = load_model()
    except FileNotFoundError:
        model, _ = train_model()
        save_model(model)
    return model


def predict_iris_species(input_data):
    model = get_or_train_model()
    feat = np.array([v for v in input_data.dict().values()]).reshape(1, -1)
    result = predict(model, feat)
    return result[0]


def retrain_model():
    model, accuracy = train_model()
    save_model(model)
    return accuracy
