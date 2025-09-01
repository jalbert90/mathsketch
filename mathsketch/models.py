from .db import Base
from sqlalchemy import Column, Integer, String, DateTime

class Predictions_Table(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)