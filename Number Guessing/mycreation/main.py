from lvl_class import Lvl
import random


checklvl = 1


def askfornewlvl():
    question = input("Do you wanna play the next lvl ? y/n :")
    print(question)
    if (question.lower() == "y"):
        createnewlvl()
    elif (question.lower() == "n"):
        print("Thanks for playing <3")
        exit()
    else:
        print("invalid token game will close")


def createnewlvl():
    global checklvl

    if (checklvl == 1):
        start_game(Lvl(1, 5, 10))
    elif (checklvl == 2):
        start_game(Lvl(2, 10, 20))
    elif (checklvl == 3):
        start_game(Lvl(3, 15, 30))
    elif (checklvl == 4):
        print("Congratz you finished the game !")


def start_game(lvl):
    global checklvl

    random_number = random.randint(lvl.firstnumber, lvl.secondnumber)
    while lvl.life > 0:
        userNumber = input(
            f"Guess a number between {lvl.firstnumber} and {lvl.secondnumber}: ", )

        try:
            userNumber = int(userNumber)
        except ValueError:
            print("Please enter a valid number.")
            continue  # Continue to the next iteration of the loop

        if userNumber == random_number:
            print("You are correct! The number is", random_number)
            checklvl += 1
            askfornewlvl()
            break  # Exit the loop if the user guesses correctly
        elif userNumber > random_number:
            print("Your number is too high. Try again.")
            lvl.life -= 1
            print("Remaining tries: ", lvl.life)
        else:
            print("Your number is too low. Try again.")
            lvl.life -= 1
            print("Remaining tries: ", lvl.life)
    if (lvl.life == 0):
        print("gameover")


createnewlvl()
