from flask import Blueprint, request, jsonify, session # Request is another global contextual object that contains information about the request itself
from app.models import User
from app.db import get_db
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

# Will resolve to the `/api/users` endpoint
@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json() # Retrieves the information from the form in a JSON object
  db = get_db()
  
  try: 
    # Attempt to create a new user
    newUser = User( # Use bracket notation to access the properties in Python. Difference between dictionaries and objects 
      username = data['username'],
      email = data['email'],
      password = data['password']
    )

    # Save in database
    db.add(newUser) # Preps the `INSERT` statement
    db.commit() # Officially updates the database
  except:
    # Insert failed, send error to the command line for internal review using the `sys` module
    print(sys.exc_info()[0]) # Tried using `exe_info` but this is not in `sys` and `exc_info` was the recommended correction
    
    # Insert failed, so rollback and send error to the front end
    db.rollback() # Rollback to prevent connections remaining in a pending state if `db.commit()` fails
    return jsonify(message = 'Signup failed'), 500  

  # This clears any existing session data and creates two new session properties
  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True

  return jsonify(id = newUser.id) # Returns a JSON object to the user/command line

# Will resolve to the `/api/users/logout` endpoint
@bp.route('/users/logout', methods=['POST'])
def logout():
  # Remove session variables
  session.clear()
  return '', 204