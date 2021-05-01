from tkinter import *
import json

def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line

def read_question(file):
    question = file.readline().strip()
    if question == '**':
        return -1
    right_answers = []
    false_answers = []
    for line in file:
        if line == '\n':
            break
        elif line[0] == '#':
            right_answers.append(line.strip()[1:])
        else:
            false_answers.append(line.strip())
    return {'question':question, 'right_answers':right_answers, 'false_answers':false_answers}


def parse_file(file_path):
    questions = []
    with open(file_path, 'r', encoding="utf8") as file:
        while True:
            tmp = read_question(file)
            if tmp != -1:
                questions.append(tmp)
            else:
                break
    return questions



if __name__ == '__main__':
    k2 = parse_file('kol2.txt')
    print('k2 gotov')
    k1 = parse_file('kol1.txt')
    print('k1 gotov')
    data_bank = {'k1':k1, 'k2': k2}
    with open('data_bank.json', 'w') as json_file:
        print('json open')
        json.dump(data_bank, json_file, indent=4)
