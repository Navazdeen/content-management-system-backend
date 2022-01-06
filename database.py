from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

import mysql.connector as connect
import os

USER = 'root'
PASSWORD = 'root'

engine = create_engine("mysql+mysqlconnector://"+USER+':' +
                       PASSWORD+"@localhost:3306/education_db", echo=False)

Base = declarative_base()


class Topic(Base):
    __tablename__ = 'topic'
    __table_args__ = {'schema': 'education_db'}

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    topic_name = Column(String(length=50), unique=True, nullable=False)

    quizz = relationship('Quizz', cascade='all, delete-orphan')
    subtopic = relationship('SubTopic', cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return f'id {self.id} | topic_name {self.topic_name} \n'


class Quizz(Base):
    __tablename__ = 'quizz'
    __table_args__ = {'schema': 'education_db'}

    question_id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey('education_db.topic.id'))
    question = Column(String(length=300))
    option1 = Column(String(length=100))
    option2 = Column(String(length=100))
    option3 = Column(String(length=100))
    option4 = Column(String(length=100))
    Anwers = Column(String(length=5))

    def __repr__(self) -> str:
        return {'question_id': {self.question_id}, 'question': {self.question}}


class SubTopic(Base):
    __tablename__ = 'sub_topic'
    __table_args__ = {'schema': 'education_db'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    subtopic_name = Column(String(length=50))
    topic_id = Column(Integer, ForeignKey('education_db.topic.id'))

    content = relationship("Content", cascade='all, delete-orphan')


class Content(Base):
    __tablename__ = 'content'
    __table_args__ = {'schema': 'education_db'}

    id = Column(Integer, primary_key=True)
    content_name = Column(String(length=50))
    content_desc = Column(String(length=500))
    topic_id = Column(Integer, ForeignKey('education_db.topic.id'))
    subtopic_id = Column(Integer, ForeignKey('education_db.sub_topic.id'))

    # topic = relationship('Topic')
    # subtopic = relationship('SubTopic')


Base.metadata.create_all(engine)


def SessionMaker():
    session_maker = sessionmaker()
    session_maker.configure(bind=engine)
    return session_maker()
