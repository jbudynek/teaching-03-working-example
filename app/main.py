from io import BytesIO
import uvicorn
from fastapi import FastAPI
from model import train_and_save_tabular, load_tabular_model
from pydantic import BaseModel
from datetime import datetime
import numpy as np

# create app

app = FastAPI()


# setup tabular model for classification
tabular_model = load_tabular_model()


class InputIrisData(BaseModel):
    """
    Input data for iris species predictions, sepal length/width, petal length/width, with defaults as the median.
    """

    sl: float = 5.8
    sw: float = 3.0
    pl: float = 4.35
    pw: float = 1.3


class OutputIrisData(BaseModel):
    """
    Output data for iris species predictions, ordinal number of species.
    """

    species: int


# BASIC ROUTES


@app.get("/")
async def root():
    """
    Simple message for homepage
    """
    return {"message": "Welcome!"}


@app.get("/hello")
async def hello():
    """
    Returns heartbeat with timestamp
    """
    return {"message": f"{datetime.now():%Y-%m-%d %H:%M:%S.%f}"}


@app.post("/predict_iris_species", response_model=OutputIrisData)
async def predict_iris_species(data: InputIrisData):
    """
    Processes numbers from input and predicts iris species.
    """
    feat = np.array([v for k, v in data.dict().items()])
    model_input = feat.reshape(1, -1)
    result = tabular_model.predict(model_input)

    return {"species": result}


@app.post("/train_iris")
async def train_iris():
    """
    Endpoint to train iris again.
    """
    train_and_save_tabular()
    tabular_model = load_tabular_model()

    return {"training": str(tabular_model)}


@app.get("/iris_report")
async def iris_report():
    """
    report
    """

    # TODO

    return {"report": "no report"}


#

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
