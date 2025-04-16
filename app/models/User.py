from app.db import Base # Import the Base class
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

salt = bcrypt.gensalt()

class User(Base): # Here we are creating a User class that inherits from the Base class
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  @validates('email')
  def validate_email(self, key, email):
    # Make sure email address contains @ character
    assert '@' in email # `assert` prompts a check. Will automatically throw an error if the condition is false, preventing the `return` statement from being called

    return email

  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4 # Check if the password length is fewer than 4 characters and throw an error if so

    # Encrypt password
    return bcrypt.hashpw(password.encode('utf-8'), salt) # Returns an encrypted version of the password if the `assert` doesn't throw an error

  def verify_password(self, password):
    return bcrypt.checkpw(
      password.encode('utf-8'),
      self.password.encode('utf-8')
    )