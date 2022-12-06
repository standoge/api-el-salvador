import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


HOST = os.environ["HOST"]

engine = create_engine(HOST)

# upper 'cause returns a class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# upper 'cause returns a class
Base = declarative_base()
