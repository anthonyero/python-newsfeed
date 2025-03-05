from flask import Blueprint, render_template # Imports the Blueprint and render_template functions from the Flask module

bp = Blueprint('home', __name__, url_prefix='/') # Blueprint() lets us consolidate routes onto a single `p` object that the parent app can register later. This corresponds to using the `Router` middleware of Express.js

# Defining a few routes
@bp.route('/')
def index():
  return render_template('homepage.html') # Using the `render_template()` function allows us to respond with a template instead of a string. 

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>') # This route uses a parameter. In the URL `<id>` represents the parameter
def single(id): # To capture the value, we include it as a function parameter - specifically, `single(id)`
  return render_template('single-post.html')