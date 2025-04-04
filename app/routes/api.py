from flask import Blueprint, request # Request is another global contextual object that contains information about the request itself
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

# Will resolve to the `/api/users` endpoint
@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json() # Retrieves the information from the form in a JSON object
  db = get_db()
  
  # Create a new user
  newUser = User( # Use bracket notation to access the properties in Python. Difference between dictionaries and objects 
    username = data['username'],
    email = data['email'],
    password = data.['password']
  )

  # Save in database
  db.add(newUser) # Preps the `INSERT` statement
  db.commit() # Officially updates the database

  return ''