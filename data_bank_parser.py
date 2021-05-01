import json

def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line

def read_question(file):
    question = file.readline()
    if question == '**':
        return -1
    correct_answers = []
    false_answers = []
    for line in file:
        if line == '\n':
            break
        elif line[0] == '#':
            correct_answers.append(line[1:].strip())
        else:
            false_answers.append(line.strip())
    return {'question': question, 'correct_answers': correct_answers, 'false_answers': false_answers}

def read_file(file_name):
    questions = []
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            question = read_question(file)
            if question == -1:
                break
            else:
                questions.append(question)
    return questions

if __name__ == '__main__':
    k1 = read_file('kol1.txt')
    k2 = read_file('kol2.txt')
    k3 = read_file('kol3.txt')
    data_bank = {'k1': k1, 'k2': k2, 'k3' : k3}

    with open('data_bank.json', 'w') as json_file:
        json.dump(data_bank, json_file, indent=4)
    
