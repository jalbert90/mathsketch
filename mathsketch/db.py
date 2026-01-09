# mathsketch/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

def get_db_url():
    DB_URL = os.getenv('DATABASE_URL')
    
    if DB_URL:
        if DB_URL.startswith('postgres://'):
            DB_URL = DB_URL.replace('postgres://', 'postgresql://', 1)
        return DB_URL
    
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']

    # Specifying the driver with +psycopg2 isn't necessary b/c default driver is picked.
    return f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# `Engine` used by `Session` to talk to DBAPI (Pyscopg2)
# Connection resources
engine = create_engine(get_db_url())

# Call `Session` (`Session()` = `sessionmaker.__call__(Session)`)
# to make a new `Session` object bound to an engine and configuration.
SessionLocal = sessionmaker(bind=engine, autoflush=False)

# Base class for ORM tables
Base = declarative_base()
