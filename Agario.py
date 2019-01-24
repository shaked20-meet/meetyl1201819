import turtle
import time
import random
import math
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
MAXIMUM_BALL_RADIUS = 101

MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5

MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

####################PART 0########################
#hoped@mit.edu

MY_BALL = Ball(0,0,1,1,10,"red")
def balls_creating():
###################################PART 3 - SMALL BALL##################################
	X_axis_speed = random.randint(-10,10)

	while X_axis_speed == 0:        #====>Makes sure the speed isn't 0 
		X_axis_speed = random.randint(-10,10)

	Y_axis_speed = random.randint(-10,10)
	while Y_axis_speed == 0:
		Y_axis_speed = random.randint(-10,10)
	#############################################################################

	for i in range (NUMBER_OF_BALLS): #==========> Creates new balls according to the list
		X_coordinate = random.randint(-200, 200)
		Y_coordinate = random.randint(-200, 200)
		radius_small = random.randint(10,150)
		color = color = (random.random(), random.random(), random.random())
		X_axis_speed = random.randint(-10,10)
		##============> Above: small ball variables, below: large ball varoables
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
		radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
		color = (random.random(), random.random(), random.random())
		big_ball = Ball(x, y, dx, dy, radius, color)
		small_ball = Ball(X_coordinate, Y_coordinate, X_axis_speed, Y_axis_speed, radius_small, color)
		BALLS.append(big_ball)#=====> appending balls to the BALLS list
		BALLS.append(small_ball)
	turtle.update()

################PART 1##########################
def move_all_balls():
	for ball in (BALLS):
		ball.move_ball(SCREEN_WIDTH, SCREEN_HEIGHT)
###############PART 2##########################
def check_collisions(ball_a, ball_b):
	if ball_a.radius == ball_b.radius:
		return False
	collide_dist = ball_a.radius + ball_b.radius
	distance = math.sqrt (math.pow(ball_a.xcor() - ball_b.xcor(),2) + math.pow(ball_a.ycor() - ball_b.ycor(),2))
	if distance + 10 <= collide_dist:
		return True
	else:
		return False
############PART 3#############################
def check_all_balls_collision():
	for ball_a in (BALLS):
		for ball_b in (BALLS):
			check_collisions(ball_a, ball_b)
			if True:
				ball_a_radius = ball_a.radius
				ball_b_radius = ball_b.radius
			
############PART 4##################################
def check_myball_collision():
	for ball in (BALLS):
		collide_dist_2 = MY_BALL.radius + ball.radius
		distance_2 = math.sqrt (math.pow(MY_BALL.xcor() - ball.xcor(),2) + math.pow(MY_BALL.ycor() - ball.ycor(),2))
		if distance_2 + 10 <= collide_dist_2:
			MY_BALL_R = MY_BALL.radius
			COLLIDE_BALL_R = ball.radius
			if MY_BALL_R < COLLIDE_BALL_R:
				return False
			else:
				balls_creating()
				MY_BALL_R += COLLIDE_BALL_R
balls_creating()
while RUNING:
	move_all_balls()
	check_all_balls_collision()
	check_myball_collision()

	turtle.update()










