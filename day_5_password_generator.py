
import random
import string      

def generate_password(length: int, use_uppercase: bool, use_numbers: bool, use_symbols: bool) -> str:
    """Generate a random password based on the specified criteria.

    Args:
        length (int): The desired length of the password.
        use_uppercase (bool): Whether to include uppercase letters.
        use_numbers (bool): Whether to include numbers.
        use_symbols (bool): Whether to include symbols.

    Returns:
        str: The generated password.
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    all_characters = lowercase + uppercase + numbers + symbols

    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password 





def main() -> None:
	"""Entry point for this script.

	Keeps the file runnable via the Run button or `python "Day 4 task.py"`.
	Currently this just prints a small header; the imported module already
	prints its own demo output when imported.
	"""
print ("Welcome to the Password Generator!")
length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

output = generate_password(length, include_uppercase, include_numbers, include_symbols)
print(f"Generated password: {output}")

if __name__ == "__main__":
	main()