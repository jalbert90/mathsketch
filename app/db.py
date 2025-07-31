from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Engine used by Session to talk to DBAPI (Pyscopg2)
# Session will use it for connection resources
engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/predictions_db")

# call Session to make a new Session object bound to an engine and configuration
Session = sessionmaker(engine)

# base class for ORM tables
Base = declarative_base()