import random
from level import Level


def play_level(level):
    secret_number = random.randint(level.start_range, level.end_range)
    attempts = level.max_attempts

    while attempts > 0:
        guess = input(f"Guess a number between {level.start_range} and {level.end_range}: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number")
            continue
        if guess == secret_number:
            print("You guessed it! Congratulations!")
            return True
        elif guess < secret_number:
            print("To low!")
        else:
            print("To high!")

        attempts -= 1
        print(f"Attempts Left : {attempts}")
    print("Out of attempts. Game over!")
    return False

def main():
    levels  = [
        Level(1,1,10,5),
        Level(2,1,20,10),
        Level(3,1,30,20),
        Level(3,1,50,30)
    ]

    for level in levels:
        print(f"Level {level.number}")
        if not play_level(level):
            break

        play_next = input("Do you want to play the next level ? (y/n): ")
        if play_next.lower() != 'y':
            break

    print("Thanks for playing")


if __name__ == "__main__":
    main()