from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  vote_count = column_property(
    select(func.count(Vote.id)).where(Vote.post_id == id) # Removed brackets around `func.count(Vote.id)` which seems to resolve the issue encountered when seeding the database. This appears to be in accordance with SQLAlchemy documentation
  )
  
  user = relationship('User')
  comments = relationship('Comment', cascade='all,delete') # Returns comments associated with post. If a post is deleted, delete all of its associated comments as well
  votes = relationship('Vote', cascade='all,delete')