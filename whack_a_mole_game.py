import turtle
import random
import time

# ----------------------
# Setup screen
# ----------------------
wn = turtle.Screen()
wn.title("Whack-a-Mole")
wn.setup(width=800, height=600)
wn.bgcolor("lightgreen")
wn.tracer(0)

# ----------------------
# Hole positions (6 holes)
# ----------------------
holes = [(-250, 150), (0, 150), (250, 150),
         (-250, -50), (0, -50), (250, -50)]

# Draw holes (visual only)
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
for x, y in holes:
    drawer.goto(x, y - 10)
    drawer.dot(70, "saddlebrown")  # hole circle

# ----------------------
# Create mole turtles (hidden initially)
# ----------------------
moles = []
mole_visible = []
for i, (x, y) in enumerate(holes):
    m = turtle.Turtle()
    m.shape("circle")
    m.color("brown")
    m.shapesize(stretch_wid=1.8, stretch_len=1.8)
    m.penup()
    m.goto(x, y)
    m.hideturtle()
    # Bind click to each mole (lambda binds current index)
    m.onclick(lambda cx, cy, idx=i: None)  # placeholder; we'll rebind below after list exists
    moles.append(m)
    mole_visible.append(False)

# Rebind properly (needs moles list ready)
def hit_mole(i):
    global score
    if not game_on:
        return
    if mole_visible[i]:
        score += 1
        mole_visible[i] = False
        moles[i].hideturtle()
        score_pen.clear()
        score_pen.write(f"Score: {score}", align="left", font=("Arial", 18, "normal"))
        wn.update()

for i, m in enumerate(moles):
    m.onclick(lambda x, y, idx=i: hit_mole(idx))

# ----------------------
# Score & Timer pens
# ----------------------
score = 0
game_duration = 30  # seconds
start_time = time.time()
game_on = True

score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(-350, 260)
score_pen.write(f"Score: {score}", align="left", font=("Arial", 18, "normal"))

timer_pen = turtle.Turtle()
timer_pen.hideturtle()
timer_pen.penup()
timer_pen.goto(250, 260)
timer_pen.write(f"Time: {game_duration}s", align="center", font=("Arial", 18, "normal"))

gameover_pen = turtle.Turtle()
gameover_pen.hideturtle()
gameover_pen.penup()

# ----------------------
# Mole show/hide logic
# ----------------------
def show_mole(idx):
    if not game_on:
        return
    if mole_visible[idx]:
        return
    moles[idx].showturtle()
    mole_visible[idx] = True
    wn.update()
    # Auto-hide after a short time if not hit
    visible_ms = random.randint(700, 1200)
    wn.ontimer(lambda i=idx: hide_mole(i), visible_ms)

def hide_mole(idx):
    if mole_visible[idx]:
        moles[idx].hideturtle()
        mole_visible[idx] = False
        wn.update()

def pop_mole():
    """Pick a random hidden mole and show it; schedule next pop."""
    if not game_on:
        return
    available = [i for i, visible in enumerate(mole_visible) if not visible]
    if available:
        idx = random.choice(available)
        show_mole(idx)
    # schedule next pop
    next_ms = random.randint(400, 900)
    wn.ontimer(pop_mole, next_ms)

# ----------------------
# Timer & end-game
# ----------------------
def update_timer():
    if not game_on:
        return
    elapsed = time.time() - start_time
    remaining = int(game_duration - elapsed)
    if remaining >= 0:
        timer_pen.clear()
        timer_pen.write(f"Time: {remaining}s", align="center", font=("Arial", 18, "normal"))
        wn.ontimer(update_timer, 250)
    else:
        end_game()

def end_game():
    global game_on
    game_on = False
    # Hide all moles
    for i in range(len(moles)):
        moles[i].hideturtle()
        mole_visible[i] = False
    # Show final message
    gameover_pen.goto(0, 0)
    gameover_pen.write(f"GAME OVER\nFinal Score: {score}",
                       align="center", font=("Courier", 30, "bold"))
    wn.update()

# ----------------------
# Instructions and start
# ----------------------
instr = turtle.Turtle()
instr.hideturtle()
instr.penup()
instr.goto(0, 200)
instr.write("Click the moles! (30 sec)  —  Click fast to score", align="center", font=("Arial", 16, "normal"))

# Start first pop and timer
wn.update()
wn.ontimer(pop_mole, 800)    # start popping after 0.8s
wn.ontimer(update_timer, 250)
wn.mainloop()
