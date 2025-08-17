# import random
#
# secret = random.randint(1, 10)
# attempts = 0
#
# while True:
#     guess = int(input("Guess a number between 1 and 10: "))
#     attempts += 1
#
#     if guess == secret:
#         print(f"🎉 Correct! You guessed in {attempts} attempts.")
#         break
#     elif guess < secret:
#         print("Too low, try again!")
#     else:
#         print("Too high, try again!")


import random

secret=random.randint(1,10)
attempt=0

while True:
    guess=int(input("Enter a number between 1 to 10:"))
    attempt=attempt+1
    if guess==secret:
        print(f"🎉 Correct! You guessed in {attempt} attempts.")
        break
    elif guess < secret:
            print("Too low, try again!")
    else:
            print("Too high, try again!")


