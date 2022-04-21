from tkinter import * 
from respondents_and_answers import DataCollectionToPassInDB
import webbrowser

main_window = Tk()
main_window.geometry('370x200')
lable_gender = Label(main_window, text="Select your gender (not mandatory)")
lable_age = Label(main_window, text = "Enter your age(not mandatory)")
var_gender_male = IntVar()
var_gender_female = IntVar()
checkbutton_gender_male = Checkbutton (main_window, text="Male", variable = var_gender_male, onvalue=1, offvalue=0)
checkbutton_gender_female = Checkbutton (main_window, text="Female", variable = var_gender_female, onvalue=1, offvalue=0 )
enter_age = Entry(main_window)

def callback(url):
    webbrowser.open_new(url)

def gender_selection():
   if (var_gender_female.get() == 1) and (var_gender_male.get() == 0):
      reciverd_gender = "Female"
   elif (var_gender_male.get() == 1) and (var_gender_female.get() == 0):
      reciverd_gender = "Male"
   else: 
      reciverd_gender = None
   return reciverd_gender

class SavingData():
      
   def submit_demografic_data(self, event):
      recived_age = enter_age.get()
      self.passing_data = DataCollectionToPassInDB(gender_value = gender_selection(), age_velue = recived_age)
      self.answer_dict()
         
   def answer_dict(self): 
      self.var_answer_selection = {}
      self.read_all_questions = self.passing_data.read_all_questions()
      for question in self.read_all_questions:
         self.var_answer_selection[question.id] = IntVar()   
      self.print_all_questions()

   def print_all_questions(self):
      questions_window = Toplevel(main_window)
      questions_window.geometry ('1000x550')
      new_row = 4
      for question in self.read_all_questions:
         new_row = new_row + 1
         one_question_at_a_time = Label (questions_window, text=f'{question.id} {question}')
         one_question_at_a_time.grid(row=new_row, column=1, columnspan= 1, sticky= W)
         
         option_1 = Radiobutton(questions_window, text= "Rarely", variable= self.var_answer_selection[question.id], value=1) #command= self.get_answer)
         option_2 = Radiobutton(questions_window, text= "Sometimes", variable=self.var_answer_selection[question.id], value=2) #command= self.get_answer)
         option_3 = Radiobutton(questions_window, text= "Often", variable=self.var_answer_selection[question.id], value=3) #command= self.get_answer)
         option_4 = Radiobutton(questions_window, text= "Always", variable=self.var_answer_selection[question.id], value=4) #command= self.get_answer)
         
         option_1.grid(row=new_row,column=2)
         option_2.grid(row=new_row,column=3)
         option_3.grid(row=new_row,column=4)
         option_4.grid(row=new_row,column=5)
      
      submit_answers = Button (questions_window, text = "Submit answers")
      submit_answers.bind("<Button-1>", respondent.result_printings)
      submit_answers.grid(row=20, column=3)

   def get_answer(self):
      for question in self.read_all_questions:
         pass_new_answer_line = self.passing_data.save_answers(respondent_id_recived = self.passing_data.read_last_respondent(), question_id_recived = question.id, answer_recived = self.var_answer_selection[question.id].get())

         # answer_list.apend(self.var_answer_selection[question.id].get())
      # print( self.var_answer_selection[1].get(), self.var_answer_selection[8].get())
      pass 

   
   def result_cauculation(self):
      self.collaborating = self.var_answer_selection[1].get() + self.var_answer_selection[5].get() + self.var_answer_selection[7].get()
      self.competing = self.var_answer_selection[4].get() + self.var_answer_selection[9].get() + self.var_answer_selection[12].get()
      self.avoiding = self.var_answer_selection[6].get() + self.var_answer_selection[10].get() + self.var_answer_selection[15].get()
      self.accommodating = self.var_answer_selection[3].get() + self.var_answer_selection[11].get() + self.var_answer_selection[14].get()
      self.compromising = self.var_answer_selection[2].get() + self.var_answer_selection[8].get() + self.var_answer_selection[13].get()
      # self.get_answer()
   
   def result_printings(self, event):
      self.result_cauculation()
      result_window = Toplevel(main_window)
      result_window.geometry ('520x250')
      instruction_text = Label (result_window, text= 'Below presented scores indicates your most commonly used conflict management strategy. \nThe one with the lowest score indicates your least preferred strategy.\n')
      result_text = Label (result_window, text= f'\nResults: \n\nCollaborating - {self.collaborating} \nCompeting - {self.competing} \nAvoiding - {self.avoiding} \nAccommodating - {self.accommodating} \nCompromising - {self.compromising}\n')
      more_information = Label(result_window, text= '  More inforation about each startagey can be found by clicking here  ', relief=SUNKEN, cursor='hand2')

      instruction_text.pack()
      result_text.pack()
      more_information.pack()
      more_information.bind('<Button-1>', lambda event: callback('https://www.valamis.com/hub/conflict-management-styles'))

submit_demografic_data_button = Button (main_window, text='Submit demografic data')
respondent = SavingData()
submit_demografic_data_button.bind("<Button-1>", respondent.submit_demografic_data)

lable_age.grid(row=0, column=2, columnspan= 2, sticky=W)
enter_age.grid(row=0, column=4, columnspan=2, sticky=W)
lable_gender.grid(row=1, column=2, columnspan= 2, sticky=W)
checkbutton_gender_male.grid(row=1,column=4)
checkbutton_gender_female.grid(row=1, column=5)
submit_demografic_data_button.grid(row=2, column=4, columnspan= 3)

main_window.mainloop()