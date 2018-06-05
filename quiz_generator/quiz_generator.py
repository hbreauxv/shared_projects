#! python3
# quiz_generator.py - generates quizzes from csv with questions and answers in
# random order, including an answer key

import random, os, shutil, csv

# Checks if you have a test folder, makes one if you dont
if not os.path.exists((os.getcwd() + '/Quiz Bank/')):
    os.makedirs(os.getcwd() + '/Quiz Bank/')

# Change directory to our tests folder so that we keep things tidy
os.chdir(os.getcwd() + '/Quiz Bank/')


testbank = {}
# Open csv file, turn it into a dictionary to be used with program
with open('testbank.csv') as csvfile:
    for row in csvfile:
        split = row.split(',')
        testbank[split[0]] = split[1]

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New' +
   ' Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West' +
   ' Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Ignore our old dictionary and use the CSV
capitals = testbank

# User inputs how many tests they wanna make
while True:
    try:
        quizAmount = int(input('How many quizzes would you like to make: '))
        break
    except ValueError:
        print('Please enter a number\n')

# User inputs the type of test
testType = input('What kind of test is this?')

for quizNum in range(quizAmount):
    # Create the quiz and answer files
    quizFile = open('quiz%s.text' % (quizNum + 1), 'w')
    answerKeyFile = open('quiz%s_answers.txt' % (quizNum + 1), 'w')

    # Write quiz header
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + '%s Quiz (Form %s)' % (testType, quizNum + 1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    # Make a question for each state
    for questionNum in range(len(capitals)):

        # Get right and wrong answer
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())

        # Delete the correct answer from our list of capitals
        del wrongAnswers[wrongAnswers.index(correctAnswer)]

        # Randomly select 3 wrong answers
        wrongAnswers = random.sample(wrongAnswers, 3)

        # Make a list of the wrong answers and the correct answer
        answerOptions = wrongAnswers + [correctAnswer]

        # Shuffle the list so that the correct answer isnt always D
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write(states[questionNum] + '\n')
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

        # Write the answer key to a file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()

# Create folder for answers
if not os.path.exists((os.getcwd() + '/answers/')):
    os.makedirs(os.getcwd() + '/answers/')

# Create folder for quizzes
if not os.path.exists((os.getcwd() + '/quizzes/')):
    os.makedirs(os.getcwd() + '/quizzes/')

# Copy files to folders
for filename in os.listdir():
    # Copy answers to answer folder, then delete them from main folder
    if filename.endswith('answers.txt'):
        shutil.copy(filename, os.getcwd() + '/answers/')
        os.unlink(filename)
    # Copy quizzes to quizzes folder, then delete them from main folder
    elif filename.endswith('.text'):
        shutil.copy(filename, os.getcwd()+ '/quizzes/')
        os.unlink(filename)