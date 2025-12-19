from day_8_caesar_cipher_art import logo
from day_7_hangman_words import word_list
import random
import os

# clear screen at start of game
def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def greet_user(someything):
    print(logo)
    print("Welcome to the Caesar Cipher Encoder/Decoder!")
    print("You can encode or decode your messages using a simple shift cipher.")
    print("Let's get started!")
    print(f"WOTD: {someything}")


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt(original_text: str, shift_amount: int) -> str:
    decrypted_text: str = ""
    for char in original_text:
        if char.isalpha():
            # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
            #  by the shift amount and print the decrypted text.
            shifted = ord(char) - shift_amount
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    print(f"Decrypted text: {decrypted_text}")
    return decrypted_text


# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text: str, shift_amount: int) -> str:
    cipher_text: str = ""
    for char in original_text:
        # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
        #  by the shift amount and print the encrypted text.
        if char.isalpha():
            shifted = ord(char) + shift_amount
            if char.islower():
                # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
                if shifted > ord('z'):
                    shifted -= 26
                cipher_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                cipher_text += chr(shifted)
        else:
            cipher_text += char
    print(f"Encrypted text: {cipher_text}")
    return cipher_text

def caesar(original_text: str, shifted_amount: int, direction: str) -> str:
    result_text: str = ""
    if direction == "decode":
            shifted_amount *= -1

    for char in original_text:

        if char.isalpha():
            shifted_position = ord(char) + shifted_amount
            if char.islower():
                if shifted_position > ord('z'):
                    shifted_position -= 26
                elif shifted_position < ord('a'):
                    shifted_position += 26
                result_text += chr(shifted_position)
            elif char.isupper():
                if shifted_position > ord('Z'):
                    shifted_position -= 26
                elif shifted_position < ord('A'):
                    shifted_position += 26
                result_text += chr(shifted_position)
        else:
            result_text += char        

    return result_text


def main():

    clear_screen()
    # some_word = random.choice(word_list)
    # greet_user(some_word)

    # TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
    #  message.
    # encrypted_message = (encrypt("Hello, World!", 5))
    # decrypted_message = (decrypt(encrypted_message, 5))

    encrypted_message =caesar("Hello, World!", 5, "encode")
    decrypted_message = caesar(encrypted_message, 5, "decode")
    print(f"caesar Encrypted message: {encrypted_message}")
    print(f"caesar Decrypted message: {decrypted_message}")


    # Further implementation of the Caesar Cipher functionality would go here.
if __name__ == "__main__":
    main()