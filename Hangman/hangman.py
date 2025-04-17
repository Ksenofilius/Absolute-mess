# HANGMAN
# Generate a random word
# Generate as many blanks as letters in the generated word
# ask the user to guess a letter
# is the guessed letter in the word?
# if Yes, then replace the blank with the letter
# if No, then lose a life
# on the Yes side, ask if all the blanks are filled
# if Yes, then it's Game Over, user won
# if No, ask for another guess
# on the No side, ask if they run out of lives
# if Yes, then it's game over, user lost
# if No, then ask for another guess


import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

