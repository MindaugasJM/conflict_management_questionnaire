from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

my_engine = create_engine('sqlite:///conflict_management/qeustions.db')
Base = declarative_base()

class DataBase(Base):
   __tablename__ = "Qestionare"
   id = Column(Integer, primary_key = True, autoincrement = True)
   # time = Column ("Time ") 
   questions = Column("Qestions", String)

   def __init__(self, questions):
       self.questions = questions

   def __repr__(self):
       return f'Qestion: {self.questions}'

Base.metadata.create_all(my_engine)