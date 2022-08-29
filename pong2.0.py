# Pong Remixed

import time
import turtle
import keyboard
import random

#Window specs & info
wn = turtle.Screen()
wn.title("Pong Remixed")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Scores
score_a = 0
score_b = 0

#Collision count
a_collisions = 0
b_collisions = 0

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
ball.dx = 0.39  # <--zcontrol-a1-- Ball's LEFT/RIGHT, HORIZONTAL, X AXIS speed
ball.dy = -0.36 # <--zcontrol-a2-- Ball's UP/DOWN, VERTICAL, Y AXIS speed

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0  Player B : 0", align="center", font=("courier", 24, "normal"))

#Center court line
center_court = turtle.Turtle()
center_court.width(2)
center_court.color("white")
center_court.hideturtle()
point1 = (0, 400)
point2 = (0, -400)
center_court.penup()
center_court.goto(point1)
center_court.pendown()
center_court.goto(point2)


# Paddle A functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 42.8
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -42.8
    paddle_a.sety(y)

# Paddle A keyboard binding while True:
wn.listen()
wn.onkeypress(paddle_a_up, "w") # <--zcontrol-a7-- Player A's paddle move UP
wn.onkeypress(paddle_a_up, "W") # <--zcontrol-a7-- Player A's paddle move UP
wn.onkeypress(paddle_a_down, "s") # <--zcontrol-a8-- Player A's paddle move DOWN
wn.onkeypress(paddle_a_down, "S") # <--zcontrol-a8-- Player A's paddle move DOWN

# Paddle B functions
def paddle_b_up():
    y = paddle_b.ycor()
    y += 42.8
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y += -42.8
    paddle_b.sety(y)

# Paddle B keyboard binding while True:
wn.listen()
wn.onkeypress(paddle_b_up, "Up") # <--zcontrol-a9-- Player B's paddle move UP
wn.onkeypress(paddle_b_down, "Down") # <--zcontrol-b1-- Player B's paddle move DOWN

while True:

    #Startup screen -- Countdown and gameplay window prep
    if ball.ycor() == 0: # <---- Probably not best but hasn't broke yet (once additional colision physics are added, could cause bug from the coordinates)
        pen.goto(0, 0)
        pen.clear()
        pen.write("3", align="center", font=("lato", 95, "normal"))
        pen.clear()
        time.sleep(1)
        pen.write("2", align="center", font=("lato", 95, "normal"))
        pen.clear()
        time.sleep(1)
        pen.write("1", align="center", font=("lato", 95, "normal"))
        pen.clear()
        time.sleep(1)
        pen.color('green')
        pen.write("START", align="center", font=("lato", 100, "normal"))
        pen.clear()
        time.sleep(.4)
        pen.color('white')
        pen.goto(0, 260)
        pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    wn.update()

    if ball.ycor() > -500 or ball.y < 500:
        point1 = (0, 400)
        point2 = (0, -400)

    #Border checking
       #Stop ball from going off screen vertically
       #Top border for ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

       #Bottom border for ball
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

        #Stop paddles from going off screen
        #Player A's paddle border
    if (paddle_a.ycor() > 245):
        paddle_a.sety(245)
    if (paddle_a.ycor() < -242):
        paddle_a.sety(-242)

        #Player B's paddle border
    if (paddle_b.ycor() > 245):
        paddle_b.sety(245)
    if (paddle_b.ycor() < -242):
        paddle_b.sety(-242)

    #Scoring and events triggered by a score
       #Ball passes paddle on right - Player A scored, ball changes to their color, point added, speed adjusted, screen flash (IF scored 3 times then winner screen is shown)
    if ball.xcor() > 395:
        ball.setx(0)
        ball.dx *= -1
        score_a += 1
        ball.color("red")
        ball.shape("circle")
        wn.bgcolor("red")
        pen.clear()
        ball.shapesize(stretch_wid=1, stretch_len=1)
        #Reset ball speed if Player A scores
        ball.dy = 0.36 # <--zcontrol-a3-- Ball's UP/DOWN, VERTICAL, Y AXIS speed
        ball.dx = 0.39 # <--zcontrol-a4-- Ball's LEFT/RIGHT, HORIZONTAL, X AXIS speed
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        time.sleep(.1)
        wn.bgcolor("black")
        #Finish game after X rounds and output Player A as winner
        if score_a > 2: # <--zcontrol-b2-- Finish game after X rounds and output Player A as winner ***Default --- score_b > 2:
            pen.clear()
            wn.clear()
            wn.bgcolor("red")
            pen.goto(0, 160)
            pen.goto(0, 160)
            pen.write("Player A Wins with:" .format(score_a, a_collisions), align="center", font=("lato", 32, "normal"))
            pen.goto(0, 100)
            pen.write("{} points" .format(score_a), align="center", font=("lato", 32, "normal"))
            pen.goto(0, 40)
            pen.write("You hit the ball {} time(s) " .format(a_collisions), align="center", font=("lato", 32, "normal"))
            print("Player A Wins with {} points and {} collisions" .format(score_a, a_collisions))
            time.sleep(3)
            break

    #Ball passes paddle on left - Player B scored, ball changes to their color, point added, speed adjusted, screen flash (IF scored 3 times then winner screen is shown)
    if ball.xcor() < -395:
        ball.setx(0)
        ball.dx *= -1
        score_b +=1
        wn.bgcolor("orange")
        ball.shape("circle")
        ball.color("orange")
        pen.clear()
        ball.shapesize(stretch_wid=1, stretch_len=1)
        #Reset ball speed if Player B scores
        ball.dy = 0.36 # <--zcontrol-a5-- Ball's UP/DOWN, VERTICAL, Y AXIS speed
        ball.dx = -0.39 # <--zcontrol-a6--Ball's LEFT/RIGHT, HORIZONTAL, X AXIS speed and changes ball direction after Player B scores so goes away from Player B's goal (***Keep negative (-) value for fair ball serving***) (or don't)
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        time.sleep(.1)
        wn.bgcolor("black")

        if score_b > 2: # <--zcontrol-b3-- Finish game after X rounds and output Player B as winner ***Default --- score_b > 2:
            print(time.time())
            time.sleep(.14)
            pen.clear()
            wn.clear()
            wn.bgcolor("orange")
            pen.goto(0, 160)
            pen.write("Player B Wins with:" .format(score_b, b_collisions), align="center", font=("lato", 32, "normal"))
            pen.goto(0, 100)
            pen.write("{} points" .format(score_b), align="center", font=("lato", 32, "normal"))
            pen.goto(0, 40)
            pen.write("You hit the ball {} time(s) " .format(b_collisions), align="center", font=("lato", 32, "normal"))
            print("Player B Wins with {} points and {} collisions" .format(score_b, b_collisions))
            time.sleep(3)
            break

    #eset ball bounce effect
    if (ball.shape() == "circle" and ball.xcor() < 300 and ball.xcor() > -300): # Normal ball bounce
        ball.shapesize(stretch_wid=1, stretch_len=1)
    if (ball.shape() == "triangle" and ball.xcor() < 210 and ball.xcor() > -210): # Nuclear attack ball bounce
        ball.shapesize(stretch_wid=4, stretch_len=4)

    #Paddles and ball collisions
       #Player A
    if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < paddle_a.ycor() + 59 and ball.ycor() > paddle_a.ycor() -59):
        ball.dx *= -1
        ball.dx *= 1.14
        ball.sety(ball.ycor() + ball.dy + 5)
        a_collisions += 1
        ball.shapesize(stretch_wid=1, stretch_len=.5)  # Squish ball/Bounce effect when hits paddle
        #Random "Super attack"
        rand = random.randrange(0, 15) # 1/15 chance - Update both player's rand variables for fair gameplay. (or don't)
        if rand < 2:
            wn.bgcolor("white")
            time.sleep(.1)
            wn.bgcolor("red")
            time.sleep(.1)
            wn.bgcolor("white")
            time.sleep(.1)
            ball.dy = 0.12
            ball.dx = 0.11
            ball.dy *= 6.1
            ball.dx *= 9.2
            wn.bgcolor("black")
            ball.color("red")
        #Nuclear Super attack
        if keyboard.is_pressed('Space'):
            ball.setheading(0)
            ball.color("red")
            ball.dy = 1.9
            ball.dx = 1.3
            ball.shape("triangle")           
            ball.shapesize(stretch_wid=2, stretch_len=4)  # Squish ball/Bounce effect when hits paddle
            wn.bgcolor("white")
            time.sleep(.1)
            wn.bgcolor("red")
            time.sleep(.1)
            wn.bgcolor("white")
            time.sleep(.2)
            wn.bgcolor("red")
            time.sleep(.2)
            wn.bgcolor("black")
            time.sleep(.1)
        #When ball collides with paddle, ball's y axis is random
        rand = random.randrange(0, 2)
        if rand < 2:
            ball.dy = -.11
        if rand < 1:
            ball.dy = .11

       #Player B
    if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < paddle_b.ycor() + 59 and ball.ycor() > paddle_b.ycor() -59):
        ball.setx(330)
        ball.dx *= -1
        ball.dx *= 1.14
        ball.sety(ball.ycor() + ball.dy + 5)
        b_collisions += 1
        ball.shapesize(stretch_wid=1, stretch_len=.5)  # Squish ball/Bounce effect when hits paddle
        #Auto Super attack
        rand = random.randrange(0, 15) # 1/15 chance - Update both player's rand variables for fair gameplay. (or don't)
        if rand < 2:
            wn.bgcolor("white")
            time.sleep(.1)
            wn.bgcolor("orange")
            time.sleep(.1)
            wn.bgcolor("white")
            time.sleep(.1)
            ball.dy = 0.12
            ball.dx = -0.11
            ball.dy *= 6.1
            ball.dx *= 9.2
            wn.bgcolor("black")
            ball.color("red")
        #Nuclear Super attack
        if keyboard.is_pressed('0'):
            ball.setheading(180)
            ball.shape("triangle")
            ball.color("orange")
            ball.dy = 1.9
            ball.dx = -1.3
            ball.shape("triangle")
            ball.shapesize(stretch_wid=2, stretch_len=4) # Squish ball/Bounce effect when hits paddle
            wn.bgcolor("white")
            time.sleep(.1)
            wn.bgcolor("orange")
            time.sleep(.1)
            wn.bgcolor("yellow")
            time.sleep(.1)
            wn.bgcolor("white")
            time.sleep(.2)
            wn.bgcolor("black")
            time.sleep(.1)

        #When ball collides with paddle, ball's y axis is random
        rand = random.randrange(0, 3)
        if rand < 2:
            ball.dy *= -1.7
        if rand > 2:
            ball.dy *= 1.6