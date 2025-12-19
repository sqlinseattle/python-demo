import sys
import os
import random
from day_7_hangman_words import word_list
from day_7_hangman_art import stages, logo

global lives_remaining 
lives_remaining = 6
global guessed_letters
guessed_letters = []

# clear screen at start of game
def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# TODO-1: - Choose a random word from the dictionary file.
def choose_word():
    chosen_word = random.choice(word_list)
    # print(chosen_word) # For testing purposes only
    return chosen_word

# TODO-1 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
def user_input():
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}'. Try again.")
        return user_input()  # Prompt the user to guess again
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
    letter_found = False
    global lives_remaining
    for letter in chosen_word:
            if letter.lower() == guess.lower():
                letter_found = True
    if not letter_found:
        lives_remaining -= 1
    return letter_found

 # Break out of choice loop and end game if win or lose condition met
def end_game(game_won=False):
    if lives_remaining == 0:
        print(f"********************You lose ! The word was {chosen_word} ***")
    elif game_won:
        print("********************You win ! ********************")
    sys.exit()   

def main():
    clear_screen()
    print(logo)
    chosen_word = choose_word()
    while lives_remaining > 0:
        guess = user_input()
        if check_letter(chosen_word, guess):
            print(f"Good guess: '{guess}' is in the word.")
        else:
            print(f"Sorry: '{guess}' is not in the word.")
        display_placeholder(chosen_word, guessed_letters)
        print(f"******************** You have {lives_remaining}/6 lives remaining. ********************")
        print(stages[lives_remaining])
if __name__ == "__main__":
    main()
