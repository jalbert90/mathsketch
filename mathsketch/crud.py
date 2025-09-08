from sqlalchemy.orm import Session
from mathsketch.models import Prediction

def save_prediction(db: Session, img_data: bytes, pred: int):
    db_entry = Prediction(image_data=img_data, prediction=pred)
    db.add(db_entry)
    db.commit()
    # So that `db_entry` has the correct attributes, such as `id`,
    # which is created by PostgreSQL when the db entry is put into the table.
    db.refresh(db_entry)