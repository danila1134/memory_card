from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QRadioButton, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QPushButton, QLabel)
from random import shuffle
from random import randint

class Question():
    def __init__(self, question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')


RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 


RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 

questions_list = []
questions_list.append(Question('Какая столица США','Вашингтон','Стамбул','Рим','Бангладеш'))
questions_list.append(Question('Самая большая по населенности страна','Китай','Индия','США','Россия'))
questions_list.append(Question('Какая столица Канады','Оттава','Порт о Пренс','Вена','Багдад'))
questions_list.append(Question('Самая большая по площади страна','Россия','Канада','США','КНР'))
questions_list.append(Question('Какая столица Бразилии','Бразилиа','Ереван','Будашепт','Гватемала'))
questions_list.append(Question('Какая столица Аргентины', 'Буэнос Айрес','Кингстон','Кампала','Вильнюс'))
questions_list.append(Question('Какая столица Португалии','Лиссабон','Лилонгве','Амстердам','Лима'))
questions_list.append(Question('Какая столица Испания','Мадрид','Варшава','Улан батор','Люксембург'))
questions_list.append(Question('Какая столица Польши','Варшава','Мехико','Катманду','Лагос'))
questions_list.append(Question('Какая столица Японии','Токио','Пекин','Кабул','Богота'))
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question()

def next_question():
    ''' задает случайный вопрос из списка '''
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)  # нам не нужно старое значение, 
                                                        # поэтому можно использовать локальную переменную! 
            # случайно взяли вопрос в пределах списка
            # если внести около сотни слов, то редко будет повторяться
    q = questions_list[cur_question] # взяли вопрос
    ask(q) # спросили

def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос

def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()


def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
q = Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
ask(q)
btn_OK.clicked.connect(check_answer) 

window.cur_question = -1
btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()
