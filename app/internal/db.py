import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///../../el_salvador_zones.db")

# upper 'cause returns a class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# upper 'cause returns a class
Base = declarative_base()


def db_connection():
    """Generates db connection for aeach request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
