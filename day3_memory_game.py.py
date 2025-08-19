import random
import time
import os


def clear_screen():
    # For Windows use 'cls', for mac/linux use 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')


print("🧠 Memory Game – Try to remember the number!")

while True:
    number = random.randint(100, 9999)  # random number with 3–4 digits
    print("Remember this number:", number)

    time.sleep(3)  # show for 3 seconds
    clear_screen()  # erase from screen

    guess = input("What was the number? ")
    if guess == str(number):
        print("✅ Correct! Great memory!\n")
    else:
        print("❌ Wrong! The number was", number, "\n")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
