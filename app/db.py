import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_HOST = os.environ["DB_HOST"]

engine = create_engine(DB_HOST)

# upper 'cause returns a class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# upper 'cause returns a class
Base = declarative_base()
