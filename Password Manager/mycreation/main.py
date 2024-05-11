
import random
import string

def determine_password_length():
    min_length = 3
    max_length = 36
    while True:
        choice = int(input("How long should the password be: "))
        if (choice >= min_length and choice < max_length):
            return choice
        else:
            print(f"Invalid choice. Please entera number between {min_length} and {max_length} ")


def determine_password_type():
    while True:
        number_choice = input(
            "Should your password have numbers ?  (y/n): ").lower()
        letter_choice = input(
            "Should your password have letters ?  (y/n): ").lower()
        symbol_choice = input(
            "Should your password have Symbols ?  (y/n): ").lower()
        
        if (number_choice == "y" and letter_choice == "y" and symbol_choice == "y"):
            criteria = create_symbols() + create_letter() + create_numbers()
            return ''.join(criteria).rstrip(", ")
        
        elif (number_choice == "n" and letter_choice == "n" and symbol_choice == "n"):
             print("You have to pick atleast one criteria")
        else:
            criteria = ""
            if number_choice == "y":
                criteria += create_numbers()
            if letter_choice == "y":
                criteria += create_letter()
            if symbol_choice == "y":
                criteria += create_symbols()

            return criteria.rstrip(", ")


def main():
    password_length = determine_password_length()
    password_type = determine_password_type()
    generated_password = ""
    length = len(password_type)
    for _ in range(password_length):
        generated_password += password_type[random.randint(0,length-1)]


    print(f"generated password: {generated_password}")


def create_letter():
    letters = list(string.ascii_letters)
    return ''.join(letters).rstrip(", ")

def create_symbols():
    symbols = list(string.punctuation)
    return ''.join(symbols).rstrip(", ")

def create_numbers():
    numbers = list(str(i) for i in range(1,10))
    return ''.join(numbers).rstrip(", ")


if __name__ == "__main__":
    main()
