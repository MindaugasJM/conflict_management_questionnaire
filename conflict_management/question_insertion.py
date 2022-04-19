from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import QuestionDataBase

engine = create_engine('sqlite:///conflict_management/Conflict_management_questionnaire.db')
session = sessionmaker(bind=engine)()

def qestion_insertion(question):
   entery = QuestionDataBase(question)
   session.add(entery)
   session.commit()

# launch this only once. Otherwise, the Questionaire db will be flooded with duplicate questions.

q_1 = qestion_insertion('I explore issues with others to find solutions that meet everyone’s needs.')
q_2 = qestion_insertion("I try to negotiate and adopt a “give-and-take” approach to problem situations.")
q_3 = qestion_insertion('I try to meet the expectations of others')
q_4 = qestion_insertion('I generally argue my case and insist on the merits of my point of view.')
q_5 = qestion_insertion("When there is a disagreement, I gather as much information as I can to keep the lines of communication open.")
q_6 = qestion_insertion("When I find myself in an argument, I usually say very little and try to leave as soon as possible")
q_7 = qestion_insertion("I try to see conflicts from both sides. What do I need? What does the other person need? What are the issues involved?")
q_8 = qestion_insertion("I prefer to compromise when solving problems and just move on.")
q_9 = qestion_insertion("I find conflicts challenging and exhilarating. I enjoy the battle of wits that usually follows.")
q_10 = qestion_insertion("Being at odds with other people makes me feel uncomfortable and anxious.")
q_11 = qestion_insertion("I try to accommodate the wishes of my friends and family.")
q_12 = qestion_insertion("I can figure out what needs to be done and I am usually right.")
q_13 = qestion_insertion("To break deadlocks, I would meet people halfway.")
q_14 = qestion_insertion("I'may not get what I want, but it is a small price to pay for keeping the peace. ")
q_15 = qestion_insertion("I avoid hard feelings by keeping my disagreements with others to myself.")