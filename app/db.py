# app/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# `Engine` used by `Session` to talk to DBAPI (Pyscopg2)
# Connection resources
engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/predictions_db")

# Call `Session` (sessionmaker.__call__()) to make a new `Session` object bound to an engine and configuration.
Session = sessionmaker(bind=engine, autoflush=False)

# Base class for ORM tables
Base = declarative_base()