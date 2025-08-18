import random

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()
    if user_choice == 'q':
        print("Thanks for playing!")
        break
    if user_choice not in options:
        print("Invalid choice. Try again!")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!\n")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You WIN!\n")
    else:
        print("You LOSE!\n")
