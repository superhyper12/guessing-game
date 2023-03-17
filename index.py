# 1. Asking the user name
# 2. Asking the user to guess the number
# 3. Bot give the guess base on the number between 1-5
# 4. Bot ask if the user guess is lower or higher than the exact answers
# 5. If User guess the number then the game end 

import random

def username():
    player_name = input("Hello, What's your name? ")
    User = player_name
    print('Okay! '+ User + ' I am guessing a number between 1-10 ') 
    return User
    
def bot_guesses():
    bot_guess = random.randrange(1,10)
    bot = bot_guess
    return bot

def user_predict(x,y):
    user_input = int(input(x + ' enter a number: '))
    while user_input != y:
        if user_input < y: 
            print('guess higher')
            user_input = int(input(' enter a number again '))
        elif user_input > y:
            print('guess lower')
            user_input = int(input(' enter a number again: '))  
        else:  
            break
        print('You have correctly guessed it!')

def main():
    x = username()
    y = bot_guesses()
    user_predict(x,y)


main()

    
    
