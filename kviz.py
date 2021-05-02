from tkinter import *
from tkinter import messagebox as mb
import json
import random

class Kviz:

    def __init__(self):
        self.corr_q = 0
        self.response = []
        self.correct_responses = []
        self.display_title()
        self.klk_frame()
        self.q_no = 0
        
    
    def q_frame(self):
        self.__bot_button('Start', self.next_question)
        self.__flash_button()
        
    def next_question(self):
        if self.check_ans():
            self.corr_q += 1

        if self.q_no==self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.destroy_frame()
            self.__bot_button('Sledece P', self.next_question)
            self.display_question(self.question_bank[self.q_no]['question'])
            self.radio_buttons(self.get_shuffled())
        self.q_no += 1

    def display_result(self):
        wrong_count = self.data_size - self.corr_q
        correct = f"Correct: {self.corr_q}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.corr_q / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self):
        for i,j in zip(self.response, self.correct_responses):
            if i.get() != j:
                return False
        return True

    def get_shuffled(self):
        self.correct_responses = []
        choices = []
        right = self.question_bank[self.q_no]['correct_answers']
        false = self.question_bank[self.q_no]['false_answers']
        r_no = len(right)
        f_no = len(false)
        while r_no or f_no:
            if (random.randint(0,2) or r_no==0) and f_no:
                self.correct_responses.append(0)
                f_no -= 1
                choices.append(false[f_no])
            elif r_no:
                self.correct_responses.append(1)
                r_no -= 1
                choices.append(right[r_no])
        return choices

    def klk_frame(self):
        self.__bot_button('Izaberi', self.chose_klk)
        self.radio_buttons(['klk1', 'klk2', 'klk3'])
        self.display_question('izaberi klk')
    
    def destroy_frame(self):
        for radio in self.radios:
            radio.destroy()
        self.bot_button.destroy()
        self.question.destroy()

    
    def display_title(self):
        title = Label(gui, text="Racunarske Mreze 1",
        width=110, bg="green",fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)
        
    def __bot_button(self, name, action):
        self.bot_button = Button(gui, text=name,command=action,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        self.bot_button.place(x=400,y=550)

    def __flash_button(self):
        self.flash_button = Button(gui, text="Flash", command=self.flash_answers,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
        self.flash_button.place(x=1000,y=50)

    def flash_answers(self):
        for bit, radio_btn in zip(self.correct_responses, self.radios):
            if bit:
                radio_btn.configure(fg='red')

    def chose_klk(self):
        self.question_bank = []
        with open('data_bank.json', 'r') as json_file:
            data_bank = json.load(json_file)
        if self.response[0].get():
            self.question_bank += data_bank['k1']
        if self.response[1].get():
            self.question_bank += data_bank['k2']
        if self.response[2].get():
            self.question_bank += data_bank['k3']
        self.destroy_frame()
        self.data_size = len(self.question_bank)
        self.q_frame()
        
    
    def display_question(self, question):
        self.question = Label(gui, text=question, width=150,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        self.question.place(x=70, y=100)

    def radio_buttons(self, questions):
        n = len(questions)
        self.response = []
        self.radios = []
        y_pos = 150
        for i in  range(0,n):
            self.response.append(IntVar())
            
            radio_btn = Radiobutton(gui,text=questions[i],variable=self.response[i],
            value = 1,font = ("ariel",14))

            self.radios.append(radio_btn)
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40

gui = Tk()
gui.geometry("1800x600")
gui.title("RM1")
kviz = Kviz()
gui.mainloop()