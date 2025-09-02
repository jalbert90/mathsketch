from mathsketch.db import engine, Base
from mathsketch.models import Predictions_Table     # Import results in class being created and logged.

# Create the table in the PostgreSQL database.
Base.metadata.createall(bind=engine)