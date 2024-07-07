import random

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    print("Enter your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Please enter your choice (1-4): ").lower()

        if user_choice == '4':
            print("Thanks for playing!")
            break
        elif user_choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter a number from 1 to 4.")
            continue

        user_choice_index = int(user_choice) - 1
        user_move = choices[user_choice_index]
        computer_move = random.choice(choices)

        print(f"\nYou chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        result = determine_winner(user_move, computer_move)
        print(result)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == "__main__":
    play_game()
