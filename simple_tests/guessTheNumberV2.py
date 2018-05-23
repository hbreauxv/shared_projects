#this program has 2 games and a main menu to choose between them.
#the games are Guess Unlimited-where you have to guess a number, and Limited Guess
#where you have to guess a number, but only get 7 tries to do it

import random

#defines the Guess Unlimited game
def guessUnlimited():

    #generates a random number for the user to guess
    secretNumber = random.randint(1,20)
    print('Im thinking of a number between 1 and 20...')

    while True:
        try:
            #has the user guess a number and then tells them if its too high or low
            userNumber = int(input('Guess the number: '))
            if userNumber > secretNumber:
                print('Your guess is too high! Guess again.')
                continue
            elif userNumber < secretNumber:
                print('Your guess is too low! Guess again.')
                continue

            #if they guess correct, tell them they won
            else:
                print('You guessed it! My number was ' + str(secretNumber))
                print('')
                break
        #error handling.  ensures the user put in a valid number    
        except ValueError:
            print('Please enter a valid number.')

#Defines the Limited Guess game 
def limitedGuess():

    #generates a random number for the user to guess
    secretNumber = random.randint(1,20)
    print('Im thinking of a number between 1 and 20...')
    
    #Limites the number of guesses the user gets to 7
    for guessLimit in range(7):
        try:
            #first we tell the user how many guesses they have left
            print('You have ' + str(7- guessLimit) + ' tries left...')

            #then we ask them to pick a number and store it
            userNumber = int(input('Guess the number: '))

            #if the number is too high or too low, tell the user and have them guess again
            if userNumber > secretNumber:
                print('Your guess is too high! Guess again')
                continue
            elif userNumber < secretNumber:
                print('Your guess is too low! Guess again')
                continue

            #if the number isn't too high or too low, they got it right! 
            else:
                break
        #ensures the user inputs a valid number
        except ValueError:
            print('Please enter a valid number')
    #checks if the user guessed the number correctly or if they ran out of tries
    if userNumber == secretNumber:
        print('You guessed it! My number was ' + str(secretNumber))
    #if they didn't guess the number, tell them the number
    else:
        print('Wrong! My number was ' + str(secretNumber))
      
            
#This is the games main menu
#We let the user pick a game and tell them how to quit
while True:
    try:
        print('')
        print('What do you want to play?')
        #asks the user to choose a game and stores it in the gameChoice variable
        gameChoice = input('Guess Unlimited or Limited Guess: ').upper()

        #launches Guess Unlimited
        if gameChoice == 'GUESS UNLIMITED':
            guessUnlimited()
        elif gameChoice == 'GUESS':
            guessUnlimited()
        #launches Limited Guess
        elif gameChoice == 'LIMITED GUESS':
            limitedGuess()
        elif gameChoice == 'LIMITED':
            limitedGuess()
        #exits the menu and ends the program
        elif gameChoice == 'EXIT':
            break

        #tells the user to type in one of the games
        else:
            print('')
            print('Choose a game or type exit to quit!')
            print('')
            continue
        
    #error handling. shouldnt end up with an unexpected error from our string input but...just in case
    except ValueError:
        print('Unexcpected input...Choose a game or type exit to quit!')

#if the user is here, its because they quit the game
print('Thanks for playing!')
