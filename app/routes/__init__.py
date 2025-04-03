from .home import bp as home # Import the Blueprint object, which contains the routes within it, and rename it `home`
from .dashboard import bp as dashboard
from .api import bp as api # Registers the API blueprint