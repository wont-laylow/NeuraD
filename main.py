from fastapi import FastAPI
from model import new_model
import torch
from schemas import Features
from datetime import datetime


app = FastAPI()

@app.get("/health")
def get_health():
    return {
        "Status": "Healthy",
        "Time": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        }


@app.post("/predict/")
def prediction(data: Features):
    data = [data.Glucose, data.BMI, data.DiabetesPedigreeFunction, data.Age]
    data = torch.tensor(data).float()

    with torch.no_grad():
        new_prediction = new_model(data)
        if new_prediction.argmax().item() == 1:
            x = "Likely Diabetes Scenario"
            print(x)
        else:
            x = "Likely Non-Diabetes Scenario"
            print(x)

        return x

