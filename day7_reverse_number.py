import random

print("🔄 Welcome to Number Reverse Puzzle! 🔢")
score = 0

while True:
    number = random.randint(100, 9999)  # 3-4 digit random number
    print("Number:", number)

    user_input = input("Type the reverse of this number (or 'q' to quit): ")

    if user_input.lower() == 'q':
        print("Thanks for playing! Final Score:", score)
        break

    # Check if input is digits
    if not user_input.isdigit():
        print("❌ Invalid input! Game Over!")
        break

    if int(user_input) == int(str(number)[::-1]):
        score += 1
        print("✅ Correct! Score:", score, "\n")
    else:
        print("❌ Wrong! The correct reverse was:", str(number)[::-1])
        print("Game Over! Final Score:", score)
        break
