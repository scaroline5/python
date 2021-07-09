import os
import random
from words import word_list
from art import logo, stages


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Print the game's logo
print(logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}. Try another letter.")

    # Clear the screen
    clear_screen()

    # Check guessed letter against the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lost a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You won.")

    print(stages[lives])
