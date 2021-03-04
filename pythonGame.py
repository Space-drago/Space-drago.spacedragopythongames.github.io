print("w key = paddle up      x key = paddle down")
print("|  < w/x | up/down > |")

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=2)
paddle_a.penup()
paddle_a.goto(-350, 0)




#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=2)
paddle_b.penup()
paddle_b.goto(350, 0)
zak = input('BG color change?(Change to black) y/n')
if zak == 'y':
 	wn.bgcolor('black')
elif zak == 'n':
	wn.bgcolor('blue')
else:
	print('AUTO COLOR BLUE')
	wn.bgcolor('blue')

vara = input("Start? ")
if vara == 'yes':
	print("GO!")
elif vara == 'no':
	input('Well then click [x]')
else:
	input("Click [x] if you do not want to play click enter to play")






#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5
#function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)
def reset():
	ball.xcor(200,200)
def colorChange():
 	wn.bgcolor(Black)

	





##
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "x")
wn.onkeypress(paddle_a_up, "W")
wn.onkeypress(paddle_a_down, "X")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(colorChange, "b")



#mainloop
while True:
	wn.update()


	#Move ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#border check
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 290:
		ball.goto(0, 0)
		ball.dx *= -1

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
	#paddle and ball collide

	if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
                ball.dx *= -1 
                
    
	if ball.xcor() > 340 and ball.ycor() > paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:     
                ball.dx *= -1
               



	






######
