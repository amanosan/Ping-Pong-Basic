import turtle
import winsound

win = turtle.Screen()
win.title("Ping Pong Basic")
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

# Scores
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# the ping pong ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Writing information:
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align='center', font=("Courier", 24, "normal"))


# functions
def paddle_a_up():
    if paddle_a.ycor() < 250:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    if paddle_a.ycor() > -240:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)


def paddle_b_up():
    if paddle_b.ycor() < 250:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    if paddle_b.ycor() > -240:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)


# key bindings
win.listen()
win.onkey(paddle_a_up, "w")
win.onkey(paddle_a_down, "s")
win.onkey(paddle_b_up, "Up")
win.onkey(paddle_b_down, "Down")

# Main Loop
while True:
    win.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    # upper border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reversing the direction of the ball

    # lower border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  # reversing the direction to start again.
        score_a += 1  # player A wins a point
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align='center', font=("Courier", 24, "normal"))

    # left border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align='center', font=("Courier", 24, "normal"))

    # paddle and ball collisions
    # paddle B
    if 340 < ball.xcor() < 350 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    # paddle A
    if -350 < ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
