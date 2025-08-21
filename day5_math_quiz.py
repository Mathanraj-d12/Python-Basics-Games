import random

score = 0

print("🧠 Math Speed Quiz Game!")
print("Type the correct answer to keep going. One mistake = GAME OVER!\n")

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    question = f"{num1} {operator} {num2}"
    correct_answer = eval(question)

    print("Question:", question)
    user_answer = input("Your answer: ")

    try:
        user_answer = int(user_answer)   # supports -7, +5, 0, etc.
    except ValueError:
        print("❌ Invalid input. Game over!")
        break

    if user_answer == correct_answer:
        score += 1
        print("✅ Correct! Score:", score, "\n")
    else:
        print("❌ Wrong! Correct answer was:", correct_answer)
        print("Game Over! Final Score:", score)
        break
