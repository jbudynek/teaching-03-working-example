from datetime import datetime

import uvicorn
from fastapi import FastAPI
from schemas import InputIrisData, OutputIrisData
from services import predict_iris_species, retrain_model

app = FastAPI()


@app.get("/")
async def root():
    """Simple message for homepage."""
    return {"message": "Welcome!"}


@app.get("/hello")
async def hello():
    """Returns heartbeat with timestamp."""
    return {"message": f"{datetime.now():%Y-%m-%d %H:%M:%S.%f}"}


@app.post("/predict_iris_species", response_model=OutputIrisData)
async def predict_species(data: InputIrisData):
    species = predict_iris_species(data)
    return {"species": species}


@app.post("/train_iris")
async def train_iris():
    accuracy = retrain_model()
    return {"accuracy": accuracy}


if __name__ == "__main__":
    print("Starting FastAPI")
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
