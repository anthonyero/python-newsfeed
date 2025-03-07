from app.db import Base # Import the Base class
from sqlalchemy import Column, Integer, String

class User(Base): # Here we are creating a User class that inherits from the Base class
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)