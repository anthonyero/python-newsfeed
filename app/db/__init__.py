from os import getenv # getenv() is part of Python's built-in `os` module
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g # Import the global variable g object for Flask application context

load_dotenv() # Call `load_dotenv()` from the `python-dotenv` module to access our `.env` file

# Connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0) # Manages the overall connection to the database
Session = sessionmaker(bind=engine) # Generates temporary connections for performing CRUD operations
Base = declarative_base() # This class variable helps us map the models to real MySQL tables

def init_db(app): # Passing `app` as a parameter
  Base.metadata.create_all(engine)

  app.teardown_appcontext(close_db) # Flask will run `close_db()` together with its built-in `teardown_appcontext()` method

def get_db():
  if 'db' not in g:
    # Store db connection in app context
    g.db = Session()

  return g.db

def close_db(e=None):
  db = g.pop('db', None) # Find and removes `db` from the `g` object

  if db is not None: # If `db` exists, then `db.close` will end the connection
    db.close()