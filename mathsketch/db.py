# mathsketch/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST', 'localhost']
DB_NAME = os.environ['DB_NAME']

# `Engine` used by `Session` to talk to DBAPI (Pyscopg2)
# Connection resources
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}')

# Call `Session` (`Session()` = `sessionmaker.__call__(Session)`)
# to make a new `Session` object bound to an engine and configuration.
SessionLocal = sessionmaker(bind=engine, autoflush=False)

# Base class for ORM tables
Base = declarative_base()
