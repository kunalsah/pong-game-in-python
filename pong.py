#pong game
#if you want game between AI VS AI then read line 280
import turtle
import winsound

#initilalising the screen
wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=900, height=700)
wn.tracer(0)

#creating the border
bd=turtle.Turtle()
bd.goto(-410,-293)
bd.pendown()
bd.pensize(22)
bd.color("red")
bd.lt(90)
bd.fd(606)
bd.penup()
bd.goto(410,313)
bd.rt(90)
bd.pendown()
bd.rt(90)
bd.fd(606)
bd.color("skyblue")
bd.rt(90)
bd.fd(820)
bd.penup()
bd.color("skyblue")
bd.goto(-410,313)
bd.lt(180)
bd.pendown()
bd.fd(820)
bd.penup()


#score
score_a = 0
score_b = 0

# adding paddle to the game
#paddle A
padA=turtle.Turtle()
padA.speed(0)
padA.shape("square")
padA.color("white")
padA.shapesize(stretch_wid=7,stretch_len=0.2)
padA.penup()
padA.goto(-380,0)

#paddle B for the AI
padB=turtle.Turtle()
padB.speed(0)
padB.shape("square")
padB.color("white")
padB.shapesize(stretch_wid=7,stretch_len=0.2)
padB.penup()
padB.goto(380,0)

#adding pong balls to the game
#inserting 1st ball in the screen
ball1=turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("red")
ball1.penup()
ball1.goto(0,0)
ball1.shapesize(stretch_wid=1,stretch_len=1)
ball1.dx= 0.25
ball1.dy= 0.25

#inserting 2nd ball in the screen
ball2=turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("deepskyblue")
ball2.penup()
ball2.goto(0,0)
ball2.shapesize(stretch_wid=1,stretch_len=1)
ball2.dx= -0.25
ball2.dy= -0.25

#inserting 3rd ball in the screen
ball3=turtle.Turtle()
ball3.speed(0)
ball3.shape("circle")
ball3.color("green")
ball3.penup()
ball3.goto(0,0)
ball3.shapesize(stretch_wid=1,stretch_len=1)
ball3.dx= 0.15
ball3.dy= 0.25

#inserting 4th ball in the screen
ball4=turtle.Turtle()
ball4.speed(0)
ball4.shape("circle")
ball4.color("yellow")
ball4.penup()
ball4.goto(0,0)
ball4.shapesize(stretch_wid=1,stretch_len=1)
ball4.dx= -0.1
ball4.dy= -0.1

#inserting 5th3rd ball in the screen
ball5=turtle.Turtle()
ball5.speed(0)
ball5.shape("circle")
ball5.color("lime")
ball5.penup()
ball5.goto(0,0)
ball5.shapesize(stretch_wid=1,stretch_len=1)
ball5.dx= 0.15
ball5.dy= 0.45

#inserting 6th ball in the screen
ball6=turtle.Turtle()
ball6.speed(0)
ball6.shape("circle")
ball6.color("cyan")
ball6.penup()
ball6.goto(0,0)
ball6.shapesize(stretch_wid=1,stretch_len=1)
ball6.dx= -0.61
ball6.dy= -0.1

#inserting 7th ball in the screen
ball7=turtle.Turtle()
ball7.speed(0)
ball7.shape("circle")
ball7.color("silver")
ball7.penup()
ball7.goto(0,0)
ball7.shapesize(stretch_wid=1,stretch_len=1)
ball7.dx= -0.15
ball7.dy= 0.35

#inserting 8th ball in the screen
ball8=turtle.Turtle()
ball8.speed(0)
ball8.shape("circle")
ball8.color("violet")
ball8.penup()
ball8.goto(0,0)
ball8.shapesize(stretch_wid=1,stretch_len=1)
ball8.dx= 0.61
ball8.dy= 0.1

#inserting 9th ball in the screen
ball9=turtle.Turtle()
ball9.speed(0)
ball9.shape("circle")
ball9.color("aqua")
ball9.penup()
ball9.goto(0,0)
ball9.shapesize(stretch_wid=1,stretch_len=1)
ball9.dx= -0.61
ball9.dy= 0.21


#creating list of balls
balls=[ball1,ball2,ball3,ball4,ball5,ball6,ball7,ball8,ball9]

#pen for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("YOU: 0 \t \t AI: 0", align="center", font=("none 24 normal"))

#function to move the paddle
#paddle A up
def padA_up():
	y=padA.ycor()
	y += 20
	padA.sety(y)

#paddle A down
def padA_down():
	y=padA.ycor()
	y -= 20
	padA.sety(y)

#paddle B up
def padB_up():
	y=padB.ycor()
	y += 20
	padB.sety(y)

#paddle B down
def padB_down():
	y=padB.ycor()
	y -= 20
	padB.sety(y)

#keyboard input
wn.listen()
wn.onkeypress(padA_up,"Up")
wn.onkeypress(padA_down,"Down")
wn.onkeypress(padB_up,"w")
wn.onkeypress(padB_down,"s")

#main game loop
while True:
	wn.update()
	for ball in balls:

		#move the ball
		ball.setx(ball.xcor()+ball.dx)
		ball.sety(ball.ycor()+ ball.dy)
	
		#border checking
		#for paddle A 
		if padA.ycor() > 230:
			padA.sety(230)

		if padA.ycor() < -210:
			padA.sety(-210)

		#for paddle B
		if padB.ycor() > 210:
			padB.sety(210)

		if padB.ycor() < -190:
			padB.sety(-190)

		#for balls
		if ball.ycor() > 290:
			ball.sety(290)
			ball.dy *= -1
			winsound.PlaySound("border_strike.wav",winsound.SND_ASYNC)

		if ball.ycor() < -270:
			ball.sety(-270)
			ball.dy *= -1
			winsound.PlaySound("border_strike.wav",winsound.SND_ASYNC)

		if ball.xcor() > 390:
			ball.goto(0,0)
			ball.dx *= -1
			score_a += 1
			pen.clear()
			pen.write("YOU: {} \t \t AI: {}".format(score_a, score_b), align="center", font=("none 24 normal"))

		if ball.xcor() < -390:
			ball.goto(0,0)
			ball.dx *= -1
			score_b += 1
			pen.clear()
			pen.write("YOU: {} \t \t AI: {}".format(score_a, score_b), align="center", font=("none 24 normal"))

		#paddle and the ball collision
		if (ball.xcor() > 370 and ball.xcor() < 380 ) and (ball.ycor() < padB.ycor() + 65 and ball.ycor() > padB.ycor() - 65):
			ball.setx(370)
			ball.dx *= -1
			winsound.PlaySound("point_lose.wav",winsound.SND_ASYNC)

		if (ball.xcor() < -370 and ball.xcor() > -380 ) and (ball.ycor() < padA.ycor() + 65 and ball.ycor() > padA.ycor() - 65):
			ball.setx(-370)
			ball.dx *= -1
			winsound.PlaySound("point_lose.wav",winsound.SND_ASYNC)


	#AI player
	closest_ball = balls[0]
	for ball in balls:
		if ball.xcor() > closest_ball.xcor():
			closest_ball = ball
		
	if padB.ycor() < closest_ball.ycor() and abs(padB.ycor() - closest_ball.ycor()) > 10:
		padB_up()

	elif padB.ycor() > closest_ball.ycor()  and abs(padB.ycor() - closest_ball.ycor()) > 10:
		padB_down() 

	#if you want AI plays against AI then UNCOMMENT remaining code otherwise don't uncomment the remaining code
	#for ball in balls:
#
	#	if ball.xcor() < closest_ball.xcor():
	#			closest_ball = ball	
#
	#if padA.ycor() < closest_ball.ycor() and abs(padA.ycor() - closest_ball.ycor()) > 10:
	#	padA_up()
#
	#elif padA.ycor() > closest_ball.ycor()  and abs(padA.ycor() - closest_ball.ycor()) > 10:
	#	padA_down() 

	