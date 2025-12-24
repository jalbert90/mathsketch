from fastapi import FastAPI, Depends
from pydantic import BaseModel
from datetime import datetime, timezone
import base64
from mathsketch.model import predict_digit
from mathsketch.db import SessionLocal
from sqlalchemy.orm import Session
from mathsketch.crud import save_prediction, get_all_predictions, delete_prediction, get_predictions
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Mount ASGI sub-app at the endpoint /static to serve files from static directory upon GET request
# to /static/... endpoints.
app.mount("/static", StaticFiles(directory="static"), "static")

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

class PredictionSchema(BaseModel):
    id: int
    image_data: str
    prediction: int
    timestamp: datetime

    class Config:
        orm_mode = True     # Allow Pydantic to read attributes of ORM object.

class DeleteRequest(BaseModel):
    ids: list[int]

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest, db: Session = Depends(get_db)):
    # FastAPI inspects the function signature ^, prepares the arguments, and then passes them upon calling.
    print(f"Base64 encoded length: {len(request.image_data)} bytes")

    try:
        img_bytes = base64.b64decode(request.image_data)
        print(f"Decoded data length: {len(img_bytes)} bytes")
    except Exception as e:
        print(f"Error decoding image data: {e}")
        raise

    pred = predict_digit(img_bytes)
    stamp = datetime.now(timezone.utc).isoformat()      # Prediction made at this time.
    save_prediction(db, img_bytes, pred)

    print(f'Prediction = {pred}')

    return PredictResponse(prediction=pred, timestamp=stamp)

@app.get("/all", response_model=list[PredictionSchema])
def get_all(db: Session = Depends(get_db)):
    return get_all_predictions(db)

@app.delete("/delete")
def delete_predictions(request: DeleteRequest, db: Session=Depends(get_db)):
    for id in request.ids:
        delete_prediction(db, id)

@app.get("/history", response_model=list[PredictionSchema])
def get_history(limit: int = 10, db: Session = Depends(get_db)):
    return get_predictions(db, limit)

@app.get("/")
def get_main_page():
    # Serve main page upon GET request to / endpoint.
    return FileResponse("static/index.html")

if __name__ == '__main__':
    import mathsketch.init_db    
    import uvicorn
    port = int(os.environ.get('PORT', 8080))
    uvicorn.run(
        'mathsketch.main:app',
        host='0.0.0.0',
        port=port
    )
