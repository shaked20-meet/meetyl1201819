import turtle
import time
import random
import CS_final_project
from CS_final_project import Ball

turtle.tracer(0)
turtle.hideturtle()
RUNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

NUMBER_OF_BALLS = 5

MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100

MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5

MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

####################PART 0########################


MY_BALL = Ball(0,0,1,1,10,"red")


for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	ball = Ball(x,y,dx, dy, radius, color)
	BALLS.append(ball)
turtle.update()

################PART 1##########################
def move_all_balls():
	for ball in (BALLS):
		ball.move_ball(SCREEN_WIDTH, SCREEN_HEIGHT)

while RUNING:
	move_all_balls()
	turtle.update()










