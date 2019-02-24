import turtle
import time
import random
import math
import CS_final_project
from CS_final_project import Ball
import pygame


turtle.tracer(0)
turtle.hideturtle()
Level = 1
SCORE = 0
RUNING = True
MAX_LEVELS = 5
SLEEP = 0.0077

Player_lost = False

SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

NUMBER_OF_BIG_BALLS = 3
NUMBER_OF_SMALL_BALLS = 2

MINIMUM_BALL_RADIUS = 51
MAXIMUM_BALL_RADIUS = 60
MY_BALL_MAX_RADIUS = 60

MINIMUM_BALL_DX = 1
MAXIMUM_BALL_DX = 3

MINIMUM_BALL_DY = 1
MAXIMUM_BALL_DY = 3

new_ball_count = 0
num_level = Level
MAX_new_ball_count = 3
BALLS = []

#turtle.register_shape("fish.gif")
#turtle.bgpic("original.gif")
MY_BALL = Ball(-100,-150,1,1,30,"red")

####################PART 0########################
#hoped@mit.edu
def init_level(Level):
	global MAXIMUM_BALL_DX
	global MAXIMUM_BALL_DY
	global NUMBER_OF_BIG_BALLS
	global NUMBER_OF_SMALL_BALLS
	global MAX_new_ball_count
	turtle.bgcolor("pink")
	if Level > 1:
		MY_BALL.goto(MY_BALL.x,MY_BALL.y)
		MAXIMUM_BALL_DX += 1
		MAXIMUM_BALL_DY += 1
		NUMBER_OF_SMALL_BALLS += 1       
		NUMBER_OF_BIG_BALLS += 1
		MAX_new_ball_count += 1
	balls_creating()
	ball_add()

def balls_creating():
	for i in range (NUMBER_OF_BIG_BALLS): #==========> Creates big balls according to the variable 'NUMBER OF BIG BALLS'
		##============>Large ball varoables

		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		dx =random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)/10
		dy =random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)/10
		radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
		color = (random.random(), random.random(), random.random())
		big_ball = Ball(0, 0, dx, dy, radius, color)
		#big_ball.shape("fish.gif")
		BALLS.append(big_ball)
		big_ball.move_ball(250,250)
	for i in range (NUMBER_OF_SMALL_BALLS):	
		##===========>Small ball variables
		X_coordinate = 0
		Y_coordinate = 0
		radius_small = random.randint(10,20)
		color = (random.random(), random.random(), random.random())
		X_axis_speed = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)/10
		Y_axis_speed = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)/10
		small_ball = Ball(X_coordinate, Y_coordinate, X_axis_speed, Y_axis_speed, radius_small, color)
		#small_ball.shape("fish.gif")
		BALLS.append(small_ball)


	turtle.update()

def ball_add():
	global num_level
	global Level
	global new_ball_count
	new_ball_count = new_ball_count + 1
	if new_ball_count <= MAX_new_ball_count:
		color_2 = (random.random(), random.random(), random.random())
		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)/10
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)/10
		RADIUS = random.randint(15,35)
		add_ball = Ball(0,0,dx,dy,RADIUS, color_2)
		BALLS.append(add_ball)                   
		add_ball.goto(random.randint(-100,100), random.randint(-100,100))       
		num_level = Level
	if Level > num_level:
		new_ball_count = 0

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
	global SCORE
	global Player_lost
	global MY_BALL
	count = 0
	count = False
	for ball in (BALLS):
		collide_dist_2 = MY_BALL.radius + ball.radius
		distance_2 = math.sqrt (math.pow(MY_BALL.xcor() - ball.xcor(),2) + math.pow(MY_BALL.ycor() - ball.ycor(),2))
		if distance_2 <= collide_dist_2:
			MY_BALL_R = MY_BALL.radius
			COLLIDE_BALL_R = ball.radius
			if MY_BALL_R < COLLIDE_BALL_R:
				Player_lost = True
				return False
			
			MY_BALL.radius = min(MY_BALL_MAX_RADIUS,(MY_BALL.radius + 5))
			MY_BALL.shapesize(MY_BALL.radius/10)
			
			BALLS.remove(ball)
			ball.hideturtle()
			score_update()
			ball_add()
			
			turtle.update()
	for ball_2 in (BALLS):
		if MY_BALL.radius < ball_2.radius:
			count += 1
		if count == len(BALLS):
			for ball_3 in (BALLS):
				ball_3.radius = ball_3.radius - 5

	return True

#########PART 5##################################
def move_around(event):
	global SCREEN_WIDTH
	global SCREEN_HEIGHT
	x = event.x - SCREEN_WIDTH
	y = SCREEN_HEIGHT - event.y
	MY_BALL.goto(x,y)
	'''
	x_list = [event.x - (SCREEN_WIDTH),-SCREEN_WIDTH, SCREEN_WIDTH]
	x_list.sort()
	MY_BALL.x = x_list[1]

	y_list = [-event.y + SCREEN_HEIGHT, SCREEN_HEIGHT, -SCREEN_HEIGHT]
	y_list.sort()
	MY_BALL.y = y_list[1]
	'''
turtle.getcanvas().bind("<Motion>", move_around)
turtle.listen()
def score_update():
	global SCORE
	turtle.hideturtle()
	turtle.penup()
	SCORE += 10
	turtle.clear()
	turtle.goto(-400,300)
	turtle.color("black")
	turtle.write("Score: " + str(SCORE), font = ("Arial", 30, "bold"))
	


def winning_banner():
	turtle.clear()
	turtle.goto(0,0)
	global Level
	if Level == 4:

		turtle.goto(0,0)
		turtle.write("YOU WON!!!", align = ("center"), font = ("Arial", 50, "bold"))
		for i in range(15):
			time.sleep(0.1)
			turtle.bgcolor(random.random(),random.random(),random.random())
	else:
		turtle.write("Level up!", align = ("center"), font = ("Arial", 50, "bold"))
		print("you won")
		time.sleep(3) 
		turtle.clear()
		MY_BALL.radius = 15
		MY_BALL.shapesize(MY_BALL.radius/10)
def loosing_banner():
	turtle.clear()
	turtle.goto(0,0)
	turtle.write("YOU LOST! :(", align = ("center"), font = ("Arial", 50, "bold"))
	print("you lost")
	time.sleep(1)

def RUN_GAME():
	global Level
	global MAX_LEVELS
	global RUNING
	while ((Level < MAX_LEVELS) and RUNING):
		print(Level)
		init_level(Level)

		while RUNING:
			SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
			SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
			move_all_balls()
			check_all_balls_collision()
			check_myball_collision()
			if len(BALLS) == 0:
				winning_banner()
				Level += 1
				break
			if Player_lost == True:
				loosing_banner()
				quit()

			#turtle.update()
	

RUN_COUNT = 0
while RUN_COUNT < MAX_LEVELS:
	pygame.init()
	pygame.mixer.music.load("mysound.mp3")
	pygame.mixer.music.play()
	RUN_COUNT += 1
	RUN_GAME()