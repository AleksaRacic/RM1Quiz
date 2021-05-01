from tkinter import *
from tkinter import messagebox as mb
import json

class Kviz:

    def __init__(self):
        self.response = []
        self.correct_responses = []
        self.display_title()
        self.klk_frame()
        self.q_no = 0
    
    def q_frame(self):
        self.__bot_button('Sledece P', self.next_question)
        
    def next_question(self):
        # Moves to next Question by incrementing the q_no counter
        
          
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
            #self.display_result()
            # destroys the GUI
            gui.destroy()
        else:
            # shows the next question
            self.display_question(self.question_bank[self.q_no]['question'])
            self.radio_buttons(self.question_bank[self.q_no]['correct_answers'])
        self.q_no += 1

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
        width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)
        
    def __bot_button(self, name, action):
        self.bot_button = Button(gui, text=name,command=action,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        self.bot_button.place(x=350,y=380)

    def quit_button(self):
        quit_button = Button(gui, text="Quit", command=gui.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
        quit_button.place(x=700,y=50)

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
        self.question = Label(gui, text=question, width=60,
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
gui.geometry("1000x450")
gui.title("RM1")
kviz = Kviz()
gui.mainloop()