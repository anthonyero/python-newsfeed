from flask import Blueprint, request, jsonify, session # Request is another global contextual object that contains information about the request itself
from app.models import User, Post, Comment, Vote
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

@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()

  # Attempt to retrieve a user from the database using the user supplied email address
  try:
    user = db.query(User).filter(User.email == data['email']).one()
  except:
    print(sys.exc_info()[0])

    return jsonify(message = 'Incorrect credentials'), 400

  # Upon successful retrieval of a user, verify the password that they provided. This utilizes the `verify_password' method we defined to the User class/model
  if user.verify_password(data['password']) == False:
    return jsonify(message = 'Incorrect credentials'), 400

  # At this point, we will have found a user in the database and verified their password, therefore we want to create a session
  session.clear() 
  session['user_id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)

@bp.route('/comments', methods=['POST'])
def comment():
  data = request.get_json()
  db = get_db()

  try:
    newComment = Comment(
      comment_text = data['comment_text'],
      post_id = data['post_id'],
      user_id = session.get('user_id')
    )

    db.add(newComment)
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Comment failed'), 500

  return jsonify(id = newComment.id)

@bp.route('/posts/upvote', methods=['PUT'])
def upvote():
  data = request.get_json()
  db = get_db()

  try:
    # Create a new vote with incoming id and session id
    newVote = Vote(
      post_id = data['post_id'],
      user_id = session.get('user_id')
    )

    db.add(newVote)
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Upvote failed'), 500

  return '', 204

@bp.route('/posts', methods=['POST'])
def create():
  data = request.get_json()
  db = get_db()

  try:
    # create a new post
    newPost = Post(
      title = data['title'],
      post_url = data['post_url'],
      user_id = session.get('user_id')
    )

    db.add(newPost)
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Post failed'), 500

  return jsonify(id = newPost.id)

@bp.route('/posts/<id>', methods=['PUT'])
def update(id):
  data = request.get_json()
  db = get_db()

  try:
    # Retrieve post and update title property
    post = db.query(Post).filter(Post.id == id).one()
    post.title = data['title']
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Post not found'), 404

  return '', 204

@bp.route('/posts/<id>', method=['DELETE'])
def delete(id):
  db = get_db()

  try:
    # Delete post from db
    db.delete(db.query(Post).filter(Post.id == id).one())
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Post not found'), 404

  return '', 204