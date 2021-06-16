# Ask  Magic 8 Ball questions and let it answer

import random

questions = {}

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes, definitely',
'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
'Signs point to yes', 'Yes', 'Reply hazy, try again', 'Ask again later',
'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
"Don't bet on it", 'My reply is no', 'My sources say no', 'Outlook not so good',
'Very doubtful']

while True:
    question = input('Ask your question:')
    if len(question) == 0: 
        break

    answer = random.choice(answers)

    if question in questions:
        print(f'Your question has already been answered: {questions[question]}')
    else:
        questions[question] = answer
        print(answer)