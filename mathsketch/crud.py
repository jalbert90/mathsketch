from sqlalchemy.orm import Session
from mathsketch.schemas import Prediction
from sqlalchemy import delete, select

def save_prediction(db: Session, img_data: bytes, pred: int):
    db_entry = Prediction(image_data=img_data, prediction=pred)
    db.add(db_entry)
    db.commit()
    # So that `db_entry` has the correct attributes, such as `id`,
    # which is created by PostgreSQL when the db entry is put into the table.
    db.refresh(db_entry)

def get_all_predictions(db: Session):
    # Create a `Select` object, which is a Python representation of an SQL SELECT statement.
    # When executed, will fetch all rows of `predictions` table and return them as
    # ORM-mapped Prediction objects.
    # Like: SELECT * FROM predictions;
    stmt = select(Prediction)
    # Execute the statement.
    # Get back a generator that yields PredictionObject
    # As opposed to (PredictionObject, ) that `execute()` would yield
    # 1 column per row = scalar (as opposed to tuple)
    # SQL executed as we iterate the generator.
    # .all() makes it into a list.
    results = db.scalars(stmt).all()
    return results

def delete_prediction(db: Session, id: int):
    stmt = delete(Prediction).where(Prediction.id==id)
    db.execute(stmt)
    db.commit()

def get_predictions(db: Session, limit: int):
    stmt = select(Prediction).order_by(Prediction.timestamp.desc()).limit(limit)
    return db.scalars(stmt).all()
