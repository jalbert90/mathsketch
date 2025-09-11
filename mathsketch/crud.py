from sqlalchemy.orm import Session
from mathsketch.models import Prediction
from sqlalchemy import delete

def save_prediction(db: Session, img_data: bytes, pred: int):
    db_entry = Prediction(image_data=img_data, prediction=pred)
    db.add(db_entry)
    db.commit()
    # So that `db_entry` has the correct attributes, such as `id`,
    # which is created by PostgreSQL when the db entry is put into the table.
    db.refresh(db_entry)

def delete_prediction(db: Session, id: int):
    stmt = delete(Prediction).where(Prediction.id==id)
    db.execute(stmt)
    db.commit()
