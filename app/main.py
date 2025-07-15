from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TestRequest(BaseModel):
    some_data: str

@app.post("/predict")
def predict_digit(request: TestRequest):
    return {"predicted_digit": 7}