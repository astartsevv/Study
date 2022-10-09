from random import randint
prompt = 'Задайте ваш вопрос '
answers = ('Да', 'Нет')
question = ''
while question != 'хватит':
    print(prompt)
    question = input()
    answer = answers[randint(0, len(answers)-1)]
    print(answer)