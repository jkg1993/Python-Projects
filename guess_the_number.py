#Importing required libraries
import random
import time
import math

def validate_input(prompt, list): #Gives a y/n prompt to the user and validates the user response.
    while True:
        requested_info = input(f'\n{prompt} ').lower() #Take user input, force it to be lowercase for simplicity.
        
        try:
            requested_info = int(requested_info) #Attempt to convert input to an integer in case the validation list is a list of integers.
        except ValueError:
            pass

        try:
            if requested_info in list:
                return requested_info
                break
            else:
                print("\nSorry, I don't recognize that response. Your response must be in the following list:\n{list}\n")
        except TypeError:
            raise Exception("One of the arguments is of the wrong type.")

def play_again(): #A function that checks if a user would like to play again.
    again = validate_input("Would you like to play again? y/n?", ['y', 'n']) #Validating that input meets expectations
    if again == 'y':
        print('\n')
        #guess()
    else:
        print("\nNo problem, I gotta run anyways. Thanks for playing!")

def user_guess(): #The version of the game where the user guesses at the conmputer's secret number.
    #Intializing the secret number to be guessed by the user.
    secret_number = random.randint(0, 1000)

    #First contact with the user.
    intro = """Alright, so you want to play a guessing game? Well I actually have a secret number which is the ultimate key to everything, \
but you'll have to figure it out. It's between 0 & 1000, and each time you guess I'll let you know if your guess is too high or too low.

How many tries will it take you to figure out the answer?"""
    print(intro)

    #Starting the game
    print("\nLet's get started guessing!\n")

    c = 0 #counter to keep track of the number of user guesses.
    while True:
        c += 1 #Adding to the count

        #Taking user input with data validation
        while True:
            try:
                user_guess = int(input(f"What is guess #{c}? ")) #taking a guess as input from the user, and then trying to convert it to an integer value.
                
                #Okay so they managed to give us an integer, but now we need to makesure that it's within the bounds we set.
                if user_guess in range(1001):
                    break
                else:
                    print("That is an integer, but you have to pick a postive number that is less than or equal to 1000. Please try again.")
            except ValueError:
                #Checking that the input is of the correct type.
                print("Whoops, you have to enter a integer value. Please try again.")
        
        difference = user_guess - secret_number #variable to determine if the player is correct.

        if difference > 0:
            print("That number is too big, try again!\n")
        elif difference < 0:
            print("That number is too small, try again!\n")
        else:
            break

    #End of the line, or is it?
    print("\nCongratulations! You did it! You now have the power to change everything, wield it with care.")
    
    play_again() #Checking if the user wants to play again.

def computer_guess():
    #First contact
    intro = """Alright, in this game mode you will pick a number between 0 & 1000, \
and I will try to guess you number in the least amount of attempts."""
    print(intro)

    while True: #Verifying if the user is ready to start.
        ready = validate_input("Have you picked a number between 0 & 1000? y/n?", ['y', 'n'])
        if ready == 'y':
            break
        else:
            print("That's ok, just take a few seconds and pick a number")
            time.sleep(random.randint(3,7))

    print("Alright, lets's get started then.\n")
    
    c = 0 #Initializing a variable to count the computer's guesses.
    lower = 0 #Intial lower boundary for valid guesses.
    upper = 1000 #Initial upper boundary for valid guesses.
    while True:
        c += 1
        possible_num = math.ceil((upper-lower)/2)
        query = validate_input(f"Guess {c}: I think it's {possible_num}\nIs that guess correct, high, or low? ", ['correct', 'high', 'low'])

        #try writing the elif function as a dictionary instead.

#debugging
#user_guess()
computer_guess()
