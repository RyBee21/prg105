"""
    Number Guessing Game 

    We Generate a number 
    You guess 
    can you win?

""""
# Important Random and Math
import math
import random

# Holds the game 
def game():

    win = random.randint(1,100) # Finds the winning number 
    print(win) # For bugging purposes

    try:

        # Keeps going until user guesses correct number 
        while win != True: # Stops when win condition reached 

            guess = int(input("What is your guess? ")) # Creates the guess variables which stores users guess 

            # Win Condition
            if guess == win: 
                print("YOU HAVE WON!!!!") # Display the win to the user
                win = True # Switch win to TRUE
                break # End
            
            # Displays how far the users guess is 
            elif 0 > abs(win - guess) <= 5:
                print("Your answer is getting very hot!!! Keep trying? ")

            elif 5 > abs(win - guess) <= 15:
                print("Your answer is hot carefully resconisder your next guess? ")

            elif 15 > abs(win - guess) <=25:
                print("Your answer is cool its ok just try again")
            
            elif abs(win - guess) > 25:
                print("Oof is answer is cold might as well go again")
            
    # Handles Values errors  
    except ValueError:
        print("This is not a valid value")

game() # Launches Game 
