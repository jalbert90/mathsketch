from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import base64

app = FastAPI()

class PredictRequest(BaseModel):
    image_data: str

class PredictResponse(BaseModel):
    predicted_digit: int
    timestamp: str

@app.post("/predict", response_model=PredictResponse)
def predict_digit(request: PredictRequest):
    print(f"Base64 encoded length: {len(request.image_data)}")

    return {"predicted_digit": 7}