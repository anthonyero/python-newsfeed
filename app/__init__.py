from app.routes import home, dashboard, api
from flask import Flask
from app.db import init_db
from app.utils import filters

def create_app(test_config=None):
  # Set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )

  @app.route('/hello')
  def hello():
    return 'hello world'

  # Register routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)

  init_db(app) # Now that we have modified `init_db` to invoke the `close_db` function and passed `app` as an argument, we no longer have to worry about connections remaining open and potentially locking up the server

  # Register custom filter functions with the Jinja template environment
  app.jinja_env.filters['format_url'] = filters.format_url
  app.jinja_env.filters['format_date'] = filters.format_date
  app.jinja_env.filters['format_plural'] = filters.format_plural

  # Any routes that we define in the `api.py` module will automatically become part of the Flask app and have a prefix of `/api`
  app.register_blueprint(api)

  return app