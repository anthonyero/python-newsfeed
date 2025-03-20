from os import getenv # getenv() is part of Python's built-in `os` module
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv() # Call `load_dotenv()` from the `python-dotenv` module to access our `.env` file

# Connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0) # Manages the overall connection to the database
Session = sessionmaker(bind=engine) # Generates temporary connections for performing CRUD operations
Base = declarative_base() # This class variable helps us map the models to real MySQL tables

def init_db():
  Base.metadata.create_all(engine)

def get_db():
  return Session() # Returns a new session-connection object