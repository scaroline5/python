from art import logo
from random import randint
import os

# Define global variables
EASY_LEVEL = 10
HARD_LEVEL = 5


def set_level():
    '''Assign the number of attempts the user will have based on the chosen difficulty'''
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL
    elif level == 'hard':
        return HARD_LEVEL
    else:
        print("Invalid difficulty chosen. Try again.")
        set_level()


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


play_again = True
while play_again:

    # Print the logo and welcome message
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Set the number of attempts
    attempts = set_level()

    # Inform how many attempts the player has based on the difficulty
    print(f"You have {attempts} attempts to guess the number.")

    # Sort a number between 1 and 100
    sorted_number = randint(1, 100)

    game_over = False

    while not game_over:
        guess = int(input("Make a guess: "))
        if guess < 1 or guess > 100:
            print("Invalid guess, try again.")
        elif guess == sorted_number:
            print(f"You got it! The answer was {sorted_number}.")
            game_over = True
        elif guess < sorted_number:
            print("Too low.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess > sorted_number:
            print("Too high.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")

        else:
            print("This is an else situation.")

        # If there are no remaining attempts, game over.
        if attempts < 1:
            print("You've run out of guesses, you lose.")
            game_over = True

        if not game_over:
            print("Guess again.")

    # Check if the player wants to play again
    valid_answer = False
    while not valid_answer:
        answer = input("Would you like to play again? Type 'yes' or 'no' ").lower()
        if answer == 'no' or answer == 'n':
            play_again = False
            valid_answer = True
        elif answer == 'yes' or answer == 'y':
            clear_screen()
            valid_answer = True
        else:
            print("Invalid answer.")
