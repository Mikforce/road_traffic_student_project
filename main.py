from Question import Question #откуда взяли class

list_of_questions = [
"На что указывает данный дорожный знак?\n(1) Впереди заграждение.\n(2) Впереди железнодорожный переезд со шлагбаумом\n(3) Движение запрещено\n\n" #\n-переход на следующую строку
]

questions = [
    Question(list_of_questions[0] , "1" )#класс применяется к этому списку : [0] , "a" - индекс вопроса - 0 , правильный ответ - а
]

def run_test(questions): #проверка верных ответов
    score = 0 #бaллы за праавильный ответ
    for question in questions: #задаем пользователю вопрос и сохраняем в переменной
        otvet = input(question.vopros)
        if otvet == question.otvet:
            score +=1
    print("У вас " + str(score)+ " балл")


run_test(questions) #запускаем тест