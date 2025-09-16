import turtle
import random

# Screen setup
wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -230)
ball.dx = 1
ball.dy = 1

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

for i in range(5):  # 5 rows
    for j in range(10):  # 10 bricks per row
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[i])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(-350 + j * 70, 250 - i * 30)
        bricks.append(brick)

# Move paddle
def paddle_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 40)

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 40)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

# Game loop
score = 0
while True:
    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        print("Game Over! Final Score:", score)
        break

    # Paddle collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if brick.isvisible() and abs(ball.xcor() - brick.xcor()) < 35 and abs(ball.ycor() - brick.ycor()) < 20:
            ball.dy *= -1
            brick.hideturtle()
            bricks.remove(brick)
            score += 10
            print("Score:", score)
