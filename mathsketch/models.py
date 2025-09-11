from .db import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

class Prediction(Base):
    # The actual table name in the database that SQL would reference:
    # INSERT INTO predictions ...
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    image_data = Column(String, nullable=False)
    prediction = Column(Integer, nullable=False)
    # Pass datetime. It is called once on class creation and used for all rows.
    # Pass callable. SQLAlchemy checks for callability then calls it everytime a new row object is created.
    # Prediction logged timestamp (client-side)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc).isoformat())
