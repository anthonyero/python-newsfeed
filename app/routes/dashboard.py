from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard') # The `url_prefix` argument allows us to prefix every route in the blueprint with `/dashboard`

@bp.route('/')
def dash():
  return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')