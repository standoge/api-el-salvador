import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


host = os.environ["HOST"]
user = os.environ["USER"]
passwd = os.environ["PASS"]

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()