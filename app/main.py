from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timezone
import base64

app = FastAPI()

class PredictRequest(BaseModel):
    image_data: str

class PredictResponse(BaseModel):
    prediction: int
    timestamp: str

@app.post("/predict", response_model=PredictResponse)
def predict_digit(request: PredictRequest):    
    print(f"Base64 encoded data: {request.image_data}")
    print(f"Base64 encoded length: {len(request.image_data)} bytes")

    try:
        img_bytes = base64.b64decode(request.image_data)
        print(f"Decoded data: {img_bytes}")
        print(f"Decoded data length: {len(img_bytes)} bytes")
    except Exception as e:
        print(f"Error decoding image data: {e}")
        raise

    timestamp = datetime.now(timezone.utc).isoformat()

    return PredictResponse(prediction=7, timestamp=timestamp)