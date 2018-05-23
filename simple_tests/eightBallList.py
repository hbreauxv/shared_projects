import random

messages = ['Yes', 'No', 'Perhaps', 'Your Mom']

while True:
    question = input('Ask the 8 Ball your question: ')
    if question.upper() == 'MIKE':
        print('Some questions only God knows the answer to...')
        continue
    if question == '':
        break
    else:
        print(messages[random.randint(0, len(messages) -1)])
    
