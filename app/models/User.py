from app.db import Base # Import the Base class
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates

class User(Base): # Here we are creating a User class that inherits from the Base class
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  @validates('email')
  def validate_email(self, key, email):
    # Make sure email address contains @ character
    assert '@' in email # `assert` prompts a check. Will automaticallythrow an error if the condition is false, preventing the `return` statement from being called

    return email