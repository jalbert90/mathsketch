from mathsketch.db import engine, Base
from mathsketch.schemas import Prediction     # Importing results in class being created and logged.

# Create the table in the PostgreSQL database.
# Pass `engine` to tell SQLAlchemy where to create the tables.
Base.metadata.create_all(bind=engine)
