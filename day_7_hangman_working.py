import sys
import os
import random

global lives_remaining 
lives_remaining = 6
global guessed_letters
guessed_letters = []

def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux/macOS (posix, osx, linux, etc.)
        _ = os.system('clear')

# TODO-1: - Update the word list to use more complex words than "cat", "dog", and "mouse"
def choose_word():
    word_list = ["ardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    print(chosen_word) # For testing purposes only
    return chosen_word


# TODO-1 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
def user_input():
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    return guess


# Create a "display_placeholder" function that prints out the placeholder and updates it when the user guesses a correct letter.
def display_placeholder(chosen_word, guessed_letters):
    placeholder = []
    game_won = True
    for letter in chosen_word:
        if letter.lower() in guessed_letters:
            placeholder.append(letter)
        else:
            placeholder.append("_")
            game_won = False
    if game_won:
        end_game(game_won=True)
        
    print(" ".join(placeholder))
    return game_won


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
def check_letter(chosen_word, guess):
    _letter_found = False
    global lives_remaining
    for letter in chosen_word:
            if letter.lower() == guess.lower():
                print(f"Right {letter}")
                _letter_found = True
            else:
                print(f"Wrong {letter}")
    if not _letter_found:
        lives_remaining -= 1

def end_game(game_won=False):
    if lives_remaining == 0:
        print("You lose.")
    elif game_won:
        print("You win.")
    sys.exit()   

def main():
    clear_screen()
    print("Let's play Hangman!")
    chosen_word = choose_word()
    while lives_remaining > 0:
        guess = user_input()
        check_letter(chosen_word, guess)
        display_placeholder(chosen_word, guessed_letters)
        print(f"You have {lives_remaining} lives remaining.")

if __name__ == "__main__":
    main()
