import random

score = 0

print("🔢 EVEN or ODD Game – Let’s test your speed & brain!")

while True:
    num = random.randint(1, 100)
    print("Number:", num)
    answer = input("Is it EVEN or ODD? ").lower()

    correct = "even" if num % 2 == 0 else "odd"

    if answer == correct:
        score += 1
        print("✅ Correct! Your score:", score, "\n")
    else:
        print("❌ Wrong! It was", correct.upper())
        print("Game Over! Final Score:", score)
        break
