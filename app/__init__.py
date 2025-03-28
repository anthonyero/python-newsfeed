from app.routes import home, dashboard
from flask import Flask
from app.db import init_db

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

  return app