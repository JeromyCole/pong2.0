# Pong

import time
import turtle

wn = turtle.Screen()
wn.title("Pong by Jeromy")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("orange")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.11
ball.dy = -0.12

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0  Player B : 0", align="center", font=("courier", 24, "normal"))

# Paddle A functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25.5
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -25.5
    paddle_a.sety(y)

# Paddle A keyboard binding while True:
wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")

# Paddle B functions
def paddle_b_up():
    y = paddle_b.ycor()
    y += 25.5
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -25.5
    paddle_b.sety(y)

# Paddle B keyboard binding while True:
wn.listen()
wn.onkey(paddle_b_up, "8")
wn.onkey(paddle_b_down, "2")

### Main game loop
while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
       #Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

       #Bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Scoring and events triggered by a score
       #Ball passes paddle on right - Player A scored, ball changes to their color, point added, speed adjusted
    if ball.xcor() > 395:
        ball.setx(0)
        ball.dx *= -1
        score_a += 1
        ball.color("red")
        wn.bgcolor("red")
        pen.clear()
        #Reset ball speed if Player A scores
        ball.dx = 0.11
        ball.dy = 0.12
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        time.sleep(.1)
        wn.bgcolor("black")
        #Finish game after X rounds and output Player A as winner
        if score_a > 2:
            pen.clear()
            wn.clear()
            wn.bgcolor("red")
            pen.goto(0, 160)
            pen.write("Player A Wins with {} points!" .format(score_a), align="center", font=("lato", 26, "normal"))
            time.sleep(5)
            break

       #Ball passes paddle on left - Player B scored, ball changes to their color, point added, speed adjusted
    if ball.xcor() < -395:
        ball.setx(0)
        ball.dx *= -1
        score_b +=1
        wn.bgcolor("orange")
        ball.color("orange")
        pen.clear()
        #Reset ball speed if Player B scores
        ball.dx = 0.11
        ball.dy = 0.12
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        time.sleep(.1)
        wn.bgcolor("black")
        #Finish game after X rounds and output Player B as winner
        if score_b > 2:
            pen.clear()
            wn.clear()
            wn.bgcolor("orange")
            pen.goto(0, 160)
            pen.write("Player B Wins with {} points!" .format(score_b), align="center", font=("lato", 26, "normal"))
            time.sleep(5)
            break

    #Paddles and ball collisions
       #Player A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.dx *= -1
        ball.dx *= 1.14
        ball.sety(ball.ycor() + ball.dy + 5)

       #Player B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        ball.dx *= 1.14
        ball.sety(ball.ycor() + ball.dy + 5)

    #Stop paddles from going off screen
       #Player A
    if (paddle_a.ycor() > 245):
        paddle_a.sety(245)
    if (paddle_a.ycor() < -242):
        paddle_a.sety(-242)

        #Player B
    if (paddle_b.ycor() > 245):
        paddle_b.sety(245)
    if (paddle_b.ycor() < -242):
        paddle_b.sety(-242)
