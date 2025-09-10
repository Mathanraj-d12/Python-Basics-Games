import turtle
import random
import time

# Screen setup
wn = turtle.Screen()
wn.title("Catch the Ball Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(random.randint(-280, 280), 250)

# Score
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Paddle movement
def paddle_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 40)

def paddle_right():
    x = paddle.xcor()
    if x < 250:
        paddle.setx(x + 40)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_left, "a")
wn.onkeypress(paddle_right, "d")

# Ball speed
fall_speed = 3

# Main loop
game_on = True
while game_on:
    wn.update()

    # Ball falling
    ball.sety(ball.ycor() - fall_speed)

    # Check if ball hits paddle
    if (ball.ycor() < -230 and 
        paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        score += 10
        fall_speed += 0.5
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
        ball.goto(random.randint(-280, 280), 250)

    # Missed ball → Game Over
    if ball.ycor() < -300:
        pen.goto(0, 0)
        pen.write(f"GAME OVER\nFinal Score: {score}", align="center", font=("Courier", 30, "normal"))
        game_on = False  # Stops the loop immediately

    time.sleep(0.01)

wn.mainloop()
