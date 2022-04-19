from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import QuestionDataBase, AnswersDataBase, RespondentDabaBase

engine = create_engine('sqlite:///conflict_management/Conflict_management_questionnaire.db')
session = sessionmaker(bind=engine)()

class DataCollection(): 
   
   def __init__(self, gender_value = None, age_velue = None):
      new_respondent = RespondentDabaBase(gender = gender_value, age = age_velue)
      self.new_respondent = new_respondent
      session.add(new_respondent)
      session.commit()
      self.new_respondent_id = new_respondent.id

   # def respondent(self, gender_value = None) :
   #    new_respondent = RespondentDabaBase(gender = gender_value)
   #    self.new_respondent = new_respondent
   #    session.add(new_respondent)
   #    session.commit()

   def answers(self):
      all_questions = session.query(QuestionDataBase).all()
      for question in all_questions:
         given_answer = input(f'{question.id} {question} present your answer here:  ')
         try: 
            given_answer is range(1,5)
            new_answer_line = AnswersDataBase(respondent_id = self.new_respondent_id, qestion_id = question.id, answer = given_answer)
            session.add(new_answer_line)
            session.commit()
         except:
            print('netinkama verte')

launch_class_DataCollection = DataCollection(gender_value = 4, age_velue = 68)
launch_class_DataCollection.answers()

