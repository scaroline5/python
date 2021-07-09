import os
import random
from art import logo


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def deal_card():
    '''Return a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    '''Take a list of cards and calculate the score based on the given cards'''
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_scores(user_score, computer_score):
    '''Compare the user score with the computer score to determine who wins'''
    if user_score > 21 and computer_score > 21:
        return "You went over. You lost. 😭"
    elif user_score == computer_score:
        return "It's a draw. 🙃"
    elif computer_score == 21:
        return "Loose, opponent has a BlackJack 😱"
    elif user_score == 21:
        return "Won with a BlackJack 😎"
    elif user_score > 21:
        return "You went over. You lost 😭"
    elif computer_score > 21:
        return "Opponent went over. You won 😁"
    elif user_score > computer_score:
        return "You won 😁"
    else:
        return "You lost 😔"


def play_game():
    # Display the Logo
    print(logo)

    # Set the variables
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial cards to user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Calculate Scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Show to user the computer's first card, their cards and score
    print(f"Computer's first card: {computer_cards[0]}")
    print(f"Your cards are {user_cards}. Your current score is {user_score}")

    while not is_game_over:

        # Check if there is a BlackJack
        if computer_score == 21 or user_score == 21 or user_score > 21:
            is_game_over = True
        else:
            # Check if the user wants another card
            user_choice = input("Do you want another card? [yes/no] 🤔\n").lower()
            # If yes, give another card to the user, calculate their score and display
            if user_choice == "yes" or user_choice == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your cards are {user_cards}. Your current score is {user_score}")
            else:
                is_game_over = True

    while computer_score != 21 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"The computer's final hand is {computer_cards}. Its final score is {computer_score}.")
    print(f"Your final hand is {user_cards}. Your final score is {user_score}.")

    # Verify and display who won
    print(compare_scores(user_score, computer_score))
    is_game_over = True


play = True
while play:
    user_choice = input("Do you want to play a game of BlackJack? [yes/no] 🃏\n").lower()
    if user_choice == "yes" or user_choice == "y":
        # Clear screen every time the game starts
        clear_screen()
        play_game()
    else:
        print("Ok. Maybe next time.")
        play = False
