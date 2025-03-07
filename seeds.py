from app.models import User
from app.db import Session, Base, engine # `engine` is the connection variable

# Drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)