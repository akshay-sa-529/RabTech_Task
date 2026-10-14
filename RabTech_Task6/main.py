# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="Sentiment Prediction API")

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

class InputData(BaseModel):
    text: str

@app.post("/predict")
def predict(data: InputData):
    X = vectorizer.transform([data.text])
    prediction = model.predict(X)[0]
    return {"text": data.text, "prediction": prediction}
