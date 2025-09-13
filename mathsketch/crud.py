from sqlalchemy.orm import Session
from mathsketch.models import Prediction
from sqlalchemy import delete, select

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

def get_predictions(db: Session):
    # Fetch ORM object Prediction
    # Like: SELECT * FROM predictions;
    stmt = select(Prediction)
    # Execute the statement.
    # Get back a generator that yields PredictionObject
    # As opposed to (PredictionObject, ) that `execute()` would yield
    # 1 column per row = scalar (as opposed to tuple)
    # SQL executed as we iterate the generator.
    # .all() makes it into a list.
    results = db.scalars(stmt)
