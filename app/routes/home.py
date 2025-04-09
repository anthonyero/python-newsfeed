from flask import Blueprint, render_template, session, redirect
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/') # Blueprint() lets us consolidate routes onto a single `p` object that the parent app can register later. This corresponds to using the `Router` middleware of Express.js

# Defining a few routes
@bp.route('/')
def index():
  # Get all posts
  db = get_db() # Returns a section connection that's tied to this route's context
  posts = db.query(Post).order_by(Post.created_at.desc()).all() # Query method on the connection object to query the `Post` model for all posts in descending order

  return render_template(
    'homepage.html', 
    posts=posts,
    loggedIn=session.get('loggedIn')
  ) # Using the `render_template()` function allows us to respond with a template instead of a string. 

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>') # This route uses a parameter. In the URL `<id>` represents the parameter
def single(id): # To capture the value, we include it as a function parameter - specifically, `single(id)`
  # Get single post by id
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # Render single post template
  return render_template(
    'single-post.html',
    post=post,
    loggedIn=session.get('loggedIn')
  )