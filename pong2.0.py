# Pong

import turtle

wn = turtle.Screen()
wn.title("Pong by Jeromy")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score A

score_a = 0
score_b = 0
#Score B

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
ball.dx = 0.08
ball.dy = -0.09

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))
# Paddle A functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)

# keyboard bindingwhile True:
wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")

# Paddle B functions
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)

# keyboard bindingwhile True:
wn.listen()
wn.onkey(paddle_b_up, "8")
wn.onkey(paddle_b_down, "2")

# Main game loop

while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 395:
        ball.setx(0)
        ball.dx *= -1
        score_a += 1
        ball.color("red")
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        if score_a > 2:
            pen.clear()
            print('Player A Wins! Good luck next time Player B...')
            break

    if ball.xcor() < -395:
        ball.setx(0)
        ball.dx *= -1
        score_b +=1
        ball.color("orange")
        #score_b += 50
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        if score_b > 2:
            pen.clear()
            print('Player B Wins! Good luck next time Player A...')
            break

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        ball.dx *= 1.14

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.dx *= -1
        ball.dx *= 1.14

    #Add Game Winner after X points