#!/usr/bin/env python

# Importing the relevant module  from python and the necessary game variables from hangman_art.py and hangman_words.py
import random
from hangman_words import word_list
from hangman_art import logo, stages


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)


# Creating blanks for the game
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, this prints the letter and lets them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Checking if user is wrong.
    if guess not in chosen_word:
        # Checking if the letter is not in the chosen_word, then printing out the letter and letting them know it's not
        # in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Joining all the elements in the list and turning it into a String.
    print(f"{' '.join(display)}")

    # Checking if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
