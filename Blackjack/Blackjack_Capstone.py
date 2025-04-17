# The purpose of the game is to add cards without
# going over the limit of 21
# Each of them cards have their value
# If you go over 21, it's called Bust which means
# you lost instantly. It doesn't matter how much over
# 21 you are, if you are you lost.
# Jack, Queen and King each counta as 10.
# Acecan either count as a 1 towards your total,
# or it can count as 11 - you decide which value it gets.
# If you both have the same total value, it's a draw.
# if one side has higher total than you, but does not
# got over 21, the other side loses.
# if someone has 21, they win instantly.
# if the dealer ends up with a hand that's samller than 17
# so 16 or under, then they must take another card.
# the dech in unlimited in size, propability is not 
# included in this game and there's no cards removing.
# more info below:
# https://www.officialgamerules.org/blackjack



import random
import os

# Create a main function for the cards
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Jack, Queen, King = 10 ; Ace = 11
    card = random.choice(cards)
    return card

# Create a function with game rules
def play_game():
    user_cards = []
    computer_cards = []
    game_over = False

    # Create a loop for cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Create a function to calculate your current score
    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        
        # Create logical behind cards
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)
    
    # Create a comparison function to determine who is winning
    def compare(user_score, computer_score):
        if user_score == 21 and user_score > computer_score:
            return "Congrats, you win!\n"     
        elif user_score == computer_score:
            return "It's a DRAW.\n"
        elif computer_score == 0:
            return "Lose, opponent has the Blackjack.\n"
        elif user_score == 0:
            return "Win with the Blackjack.\n"
        elif user_score > 21:
            return "Nie no, tyle to nie. You lose.\n"
        elif computer_score > 21:
            return "Opponent jumped off a bridge. You win.\n"
        elif user_score > computer_score:
            return" You win"
        else:
            return "You lose, loser.\n"

    # Create a loop for the game
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Create a loop for dealing the cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_score}, final score: {computer_score}\n")

    print(compare(user_score, computer_score))

# Continue?
while input("Do you want to play a game of Blackjack? Type 'y' for yes, and 'n' for no: ") == 'y':
    os.system('cls')
    play_game()
    