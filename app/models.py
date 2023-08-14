from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String
from sqlalchemy.sql.expression import text
from .database import Base 

#region Models
class Post(Base):
    __tablename__ = "tblPosts"
    
    Id = Column(Integer, primary_key=True, nullable=False)
    Title = Column(String, nullable=False)
    Content = Column(String, nullable=False)
    Published = Column(Boolean, server_default='True', nullable=False)
    CreatedDate = Column(TIMESTAMP(timezone=True),server_default=text('now()'), nullable=False)
    
class User(Base):
    __tablename__ = "tblUsers"
    
    Id = Column(Integer, primary_key=True, nullable=False)
    Email = Column(String, nullable=False, unique=True)
    Password = Column(String, nullable=False)
    CreatedDate = Column(TIMESTAMP(timezone=True),server_default=text('now()'), nullable=False)
#endregion