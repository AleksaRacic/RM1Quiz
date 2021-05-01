from tkinter import *
from tkinter import messagebox as mb
import json

def destroy_objects(objects):
    for gui_object in objects:
        gui_object.grid_forget()

class Quiz:

    def __init__(self, data_bank):

        self.q_no = 0

    def radio_buttons(self, choices):
        options = [len(choices) * 0]
        btn_list =[]
        y_pos = 150
        for i in range(0,len(choices)):
            radio_btn = Radiobutton(gui,
                                    text=choices[i],
                                    variable=options,
                                    value=1,
                                    font=('ariel', 14))
            btn_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40

        return btn_list, options

    def chose_klk(self, data_bank):
        self.question_bank = []
        self.dislay_question('Izaberite kolokvijume')
        btn_list, options = self.radio_buttons(self, ['Prvi Kolokvijum', 'Drugi kolokvijum'])


    def display_question(self, question):

        question = Label(gui,
                         text=question,
                         wirdth=60,
                         font=('ariel', 16, 'bold'),
                         anchor='w')
        question.place(x=70, y=100)

gui = Tk()

with open('data_bank.json', 'r') as file:
    data = json.load(file)

quiz = Quiz
gui.mainloop()
