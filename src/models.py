import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    user_id =Column(String(250), nullable=False, ForeignKey)

class Storys(Base):
    __tablename__ = 'storys'
    user_id = Column(Integer, ForeignKey("users.user_id")
    comentary = Column(String(250))
    date = Column(Integer)
    users = relationship(users)

class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey("users.user_id")
    summary = Column(String(250))
    date = Column(Integer)
    users = relationship(users)

class Chat(Base):
    __tablename__ = 'chat'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey("users.user_id")
    name_friend = Column(String(250))
    emoticons = Column(String(250))
    date = Column(Integer)
    users = relationship(users)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e