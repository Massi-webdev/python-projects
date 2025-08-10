import turtle #let's start by importing turtle

# SO we start by defining the window properties and name.
win = turtle.Screen()
win.title('Pong')
win.bgcolor('black')
win.setup(width=800, height=600)



## Now, we create all drawing objects, we will use in the game (2paddles and a ball)
#creating paddle 1 of player 1
paddleA = turtle.Turtle() #new drawing object
paddleA.speed(0) #fastest drawing speed
paddleA.shape('square')
paddleA.color('yellow')
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup() # to not draw line when moving the block
paddleA.goto(-350, 0)

#creating paddle 2 of player 2
paddleB = turtle.Turtle() #new drawing object
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('yellow')
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup() # to not draw line when moving the block
paddleB.goto(350, 0)

#creating the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0,0)
ball.dx = 6 #ball velocity
ball.dy = 6 #ball velocity

## Now we will create score and display and pen to write score on screen
scoreA=0
scoreB=0
pen = turtle.Turtle()
pen.speed(0)
pen.color('aquamarine')
pen.penup()
pen.hideturtle() # to hide the cursor
pen.goto(0, 260)
pen.write("Player A: 0   -  Player B: 0", align='center', font=('Arial', 20, 'normal'))


## Lets create functions to move paddles
# Player 1
def paddleA_up():
    y = paddleA.ycor()
    if y <240:
        y+=20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    if y >-240:
        y-=20
    paddleA.sety(y)

#player 2
def paddleB_up():
    y = paddleB.ycor()
    if y <250:
        y+=20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    if y >-235:
        y-=20
    paddleB.sety(y)

## now we will create bindings
win.listen() #this is equivalent to eventlisteners in js
# tell windows to listen to events

# Player 1
win.onkeypress(paddleA_up, 'w')
win.onkeypress(paddleA_down, 's')
# Player 2
win.onkeypress(paddleB_up, 'Up')
win.onkeypress(paddleB_down, 'Down')


## The most important part: the game logic

while True: #keep the game running with an infinite loop
    # Move the ball by getting the current position using xcor and add the horizontal or vertical change
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Manage ball collisions
    # if ball is above 290, it is stopped and reversed
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Manage scoring and updating it when losing/winning
    if ball.xcor() > 390:
        scoreA += 1
        pen.clear()
        #update score
        pen.write(f"Player A: {scoreA}    Player B: {scoreB}", align="center", font=("Courier", 20, "normal"))
        ball.goto(0, 0) #reset the ball position
        ball.dx *= -1 # mov ball towards the other player

    if ball.xcor() < -390:
        scoreB += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}    Player B: {scoreB}", align="center", font=("Courier", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    #Handle ball paddle collisions
    # see if ball is near paddleB position 340-350 range
    #and
    # see if ball position is within the paddle center
    # if true then stop the ball and reverse it
    if (340 < ball.xcor() <350) and (paddleB.ycor() - 50 < ball.ycor() < paddleB.ycor() + 50):
        ball.setx(340)

        # we can make game challenging by accelerating ball each time
        ball.dx *= -1.05
        ball.dy *= -1.05
    if (-350 < ball.xcor() <-330) and (paddleA.ycor() - 50 < ball.ycor() < paddleA.ycor() + 50):
        ball.setx(-330)
        ball.dx *= -1.05
        ball.dy *= -1.05

turtle.done()