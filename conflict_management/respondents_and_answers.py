from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import QuestionDataBase, AnswersDataBase, RespondentDabaBase

engine = create_engine('sqlite:///conflict_management/Conflict_management_questionnaire.db')
session = sessionmaker(bind=engine)()

class DataCollectionToPassInDB(): 
   
   def __init__(self, gender_value = None, age_velue = None):
      new_respondent = RespondentDabaBase(gender = gender_value, age = age_velue)
      self.new_respondent = new_respondent
      session.add(new_respondent)
      session.commit()
      self.new_respondent_id = new_respondent.id

   def read_all_questions(self):
      all_questions = session.query(QuestionDataBase).all()
      return all_questions

   def read_last_respondent(self):
      respondent_id = session.query(RespondentDabaBase).all()
      return respondent_id

   def save_answers(self, respondent_id_recived, question_id_recived, answer_recived):
      # all_questions = session.query(QuestionDataBase).all()
      # for question in all_questions:
         # given_answer = int(input(f'{question.id} {question} present your answer here:  '))
      new_answer_line = AnswersDataBase(respondent_id = respondent_id_recived, question_id = question_id_recived, answer = answer_recived)
      session.add(new_answer_line)
      session.commit()
      
      # new_respondent_id, question_id = question.id, answer = given_answer)

      

# launch_class_DataCollection = DataCollection(gender_value = 4, age_velue = 68)
# launch_class_DataCollection.answers()

