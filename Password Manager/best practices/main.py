import random
import string

def determine_password_length():
    min_length = 3
    max_length = 36
    while True:
        try:
            choice = int(input("How long should the password be: "))
            if(min_length <= choice < max_length):
                return choice
            else:
                print(f"Invalid choice. Pleas enter a number between {min_length} and {max_length}")
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def determine_password_type():
    number_choice = input("Should your password have numbers? (y/n): ").lower()
    letter_choice = input("Should your password have letters? (y/n): ").lower()
    symbol_choice = input("Should your password have symbols? (y/n): ").lower()

    criteria = []

    if number_choice == "y":
        criteria.extend(create_numbers())
    if letter_choice == "y":
        criteria.extend(create_letters())
    if symbol_choice == "y":
        criteria.extend(create_symbols())

    if criteria:
        return criteria
    else:
        print("You have to pick at least one criteria")
        return determine_password_type()
    

def main():
    password_length = determine_password_length()
    password_type = determine_password_type()
    generated_password = ''.join(random.choices(password_type, k=password_length))
    print(f"Generated password: {generated_password}")

def create_letters():
    return string.ascii_letters


def create_symbols():
    return string.punctuation


def create_numbers():
    return string.digits


if __name__ == "__main__":
    main()