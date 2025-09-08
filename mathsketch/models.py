from .db import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    image_data = Column(String, nullable=False)
    prediction = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc).isoformat())