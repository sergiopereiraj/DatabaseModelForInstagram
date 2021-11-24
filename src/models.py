import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    storys = relationship("Storys")
    posts = relationship("Posts")
    chats = relationship("Chats")

class Story(Base):
    __tablename__ = 'storys'
    id = Column(Integer, primary_key=True)
    comentary = Column(String(250), nullable=False)
    date = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    summary = Column(String(250), nullable=False)
    date = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

class Chat(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True)
    name_friend = Column(String(250), nullable=False)
    emoticons = Column(String(250), nullable=False)
    date = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e