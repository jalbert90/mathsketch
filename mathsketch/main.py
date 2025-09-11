from fastapi import FastAPI, Depends
from pydantic import BaseModel
from datetime import datetime, timezone
import base64
from mathsketch.model import predict_digit
from mathsketch.db import SessionLocal
from sqlalchemy.orm import Session
from mathsketch.crud import save_prediction, delete_prediction

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class PredictRequest(BaseModel):
    image_data: str

class PredictResponse(BaseModel):
    prediction: int
    timestamp: str

@app.post("/predict", response_model=PredictResponse)
def predict_endpoint_actions(request: PredictRequest, db: Session = Depends(get_db)):
    # FastAPI inspects the function signature ^, prepares the arguments, and then passes them upon calling.
    print(f"Base64 encoded length: {len(request.image_data)} bytes")

    try:
        img_bytes = base64.b64decode(request.image_data)
        print(f"Decoded data length: {len(img_bytes)} bytes")
    except Exception as e:
        print(f"Error decoding image data: {e}")
        raise

    # pred = predict_digit(img_bytes)
    pred = 4
    stamp = datetime.now(timezone.utc).isoformat()      # Prediction made timestamp
    save_prediction(db, img_bytes, pred)
    delete_prediction(db, 1)

    return PredictResponse(prediction=pred, timestamp=stamp)
