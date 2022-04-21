from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

my_engine = create_engine('sqlite:///conflict_management/Conflict_management_questionnaire.db')
Base = declarative_base()

class QuestionDataBase(Base):
   __tablename__ = "Questions"
   id = Column(Integer, primary_key = True, autoincrement = True)
   questions = Column("Question", String)

   def __init__(self, questions):
       self.questions = questions

   def __repr__(self):
       return self.questions

class RespondentDabaBase(Base):
    __tablename__ = "Respondent"
    id = Column(Integer, primary_key = True, autoincrement = True)
    gender = Column("Gender", String, nullable = True)
    age = Column("Age", Integer, nullable = True)

    def __repr__(self):
        return self.id

class AnswersDataBase(Base):
    __tablename__ = "Answers"
    id = Column(Integer, primary_key = True, autoincrement = True)
    respondent_id = Column(Integer, ForeignKey('Respondent.id'))
    question_id = Column(Integer, ForeignKey('Questions.id'))
    answer = Column("Answer", Integer)

Base.metadata.create_all(my_engine)