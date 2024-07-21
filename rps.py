import random #import random is used to generate random choices for the computer.


def get_computer_choice(): #Returns a random choice
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice(): # Prompts the user to enter choice
    user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice): #Determines the winner based on the rules.
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 3 #Plays 3 rounds

    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            print("You win this round!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a tie!")

    print("\nFinal Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    if user_score > computer_score:#Prints the final scores and announces the overall winner.
        print("Congratulations! You are the overall winner!")
    elif computer_score > user_score:
        print("Computer is the overall winner. Better luck next time!")
    else:
        print("It's an overall tie!")
#This code allows you to play a 3-round game of  against the computer and see who wins overall.
# Play the game
play_game()
