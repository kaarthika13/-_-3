import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """Generates a random password based on user preferences."""
    if not any([use_letters, use_numbers, use_symbols]):
        print("Error: At least one character type must be selected.")
        return None

    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    """Handles user input and generates the password."""
    try:
        length = int(input("Enter the password length: "))
        if length <= 0:
            print("Error: Password length must be greater than 0.")
            return

        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Error: Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
