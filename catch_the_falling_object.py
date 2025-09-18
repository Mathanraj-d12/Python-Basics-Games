import turtle
import random

# Screen setup
wn = turtle.Screen()
wn.title("Catch the Falling Objects")
wn.bgcolor("skyblue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Basket
basket = turtle.Turtle()
basket.shape("square")
basket.color("brown")
basket.shapesize(stretch_wid=1, stretch_len=5)
basket.penup()
basket.goto(0, -250)

# Falling object
fruit = turtle.Turtle()
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(random.randint(-280, 280), 250)

# Score
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-250, 260)
pen.write(f"Score: {score}", font=("Arial", 18, "normal"))

# Controls
def move_left():
    x = basket.xcor()
    if x > -260:
        basket.setx(x - 40)

def move_right():
    x = basket.xcor()
    if x < 260:
        basket.setx(x + 40)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

game_on = True

def game_loop():
    global score, game_on
    if not game_on:
        return

    # Move fruit down
    fruit.sety(fruit.ycor() - 20)

    # Catch check
    if fruit.ycor() < -230 and abs(fruit.xcor() - basket.xcor()) < 50:
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", font=("Arial", 18, "normal"))
        fruit.goto(random.randint(-280, 280), 250)

    # Missed fruit
    elif fruit.ycor() < -280:
        game_on = False
        pen.goto(0, 0)
        pen.write(f"GAME OVER\nFinal Score: {score}", align="center", font=("Arial", 24, "bold"))

    wn.update()
    wn.ontimer(game_loop, 100)  # run again after 100 ms (10 FPS)

# Start game loop
game_loop()
wn.mainloop()


