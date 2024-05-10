import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (Rock/Paper/Scissors): ").lower()
        if choice in ['rock','paper','scissors']:
            return choice
        else:
            print("Invalid choice. Please enter 'Rock, 'Paper', or 'Scissors.")


def get_computer_choice():
    return random.choice(['rock','paper','scissors'])

def determine_winner(player_choice, cp_choice):
    if player_choice == cp_choice:
        return 'Draw'
    elif(player_choice == 'rock' and cp_choice == 'scissors')or \
        (player_choice == 'paper' and cp_choice == 'rock') or \
        (player_choice == 'scissors' and cp_choice == 'paper'):
        return 'Player'
    else:
        return 'CP'
    

def main():
    print("Welcome to Rock Paper Scissors")
    rounds = int(input("How many round do you want to play? "))
    player_counter = 0
    cp_counter = 0

    for _ in range(rounds):
        player_choice = get_user_choice()
        cp_choice = get_computer_choice()
        print(f"Player Choice: {player_choice}, CP Choice: {cp_choice}")

        winner = determine_winner(player_choice,cp_choice)
        if winner == "Draw":
            print("--Draw--")
        else:
            print(f"--{winner} Wins--")
            if winner == "Player":
                player_counter += 1
            else:
                cp_counter += 1
    result = "Player" if player_counter > cp_counter else "CP"
    print(f"Game over! The winner is: {result}" )

if __name__ =="__main__":
    main()   