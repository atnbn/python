import random

def main():
    computer_choices = [
        'rock', 'paper' ,'scissors'
    ]
    player_counter = 0
    cp_counter = 0
    print("Welcome to Rock Paper Scissors")
    rounds = input("How many Rounds do you wanna play ?")

    try:
            rounds = int(rounds)
    except ValueError:
            print("Please enter a valid choice")
    while rounds > 0:
        cp_choice = computer_choices[random.randint(0, 2)]
        player_choice = input("Enter your choice \n Rock \n Paper \n Scissors \n ")
        print(f"Player Choice {player_choice}. Cp Choice {cp_choice}",)
        try:
            player_choice = str(player_choice)
        except ValueError:
            print("Please enter a valid choice")
        if (player_choice.lower() == cp_choice):
            print("--Draw--")

            rounds -= 1
        elif player_choice.lower() == "rock" and cp_choice == "paper":
            print("--Computer Wins--")

            cp_counter += 1
            rounds -= 1
        elif player_choice.lower() == "rock" and cp_choice == "scissors":
            print("--Player Wins--")

            player_counter += 1
            rounds -= 1
        elif player_choice.lower() == "scissors" and cp_choice == "rock":
            print("--Computer Wins--")

            cp_counter += 1
            rounds -= 1
        elif player_choice.lower() == "scissors" and cp_choice == "paper":
            print("--Player Wins--")

            player_counter +=1
            rounds -= 1
        elif player_choice.lower() == "paper" and cp_choice == "rock":
            print("--Player Wins--")

            player_counter += 1
            rounds -= 1
        elif player_choice.lower() == "paper" and cp_choice == "scissors":
            print("--Computer Wins--")
            cp_counter += 1
            rounds -= 1
        else :
            print("Invalid answer")
    result ="Player" if player_counter > cp_counter else "CP"
    print(f"Game is over the Winner is: {result}")



if __name__ == "__main__":
    main()