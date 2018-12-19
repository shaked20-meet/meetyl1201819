#############
import turtle
from turtle import *
turtle.colormode(255)
import random
import math
#list of balls
ball_list = []
ball_index = 0
turtle.tracer(0)
#this class defines the border 
class SquaredBorder(Turtle):
	def __init__(self, top_left_x, top_left_y, length):
		Turtle.__init__(self)
		self.top_left_x  = top_left_x
		self.top_left_y = top_left_y
		self.length = length
	def make_square(self):
		self.hideturtle()
		self.penup()
		self.goto(self.top_left_x,self.top_left_y)
		self.pendown()
		self.goto(self.top_left_x + self.length, self.top_left_y)
		self.goto(self.top_left_x + self.length, self.top_left_y - self.length)
		self.goto(self.top_left_x, self.top_left_y - self.length)
		self.goto(self.top_left_x, self.top_left_y)
	def min_x(self):
		return (self.top_left_x)
	def max_x(self):
		return (self.top_left_x + self.length)

#this class creates the balls	
class Ball(Turtle):
	def __init__(self, radius, color, speed,dx,dy):
		global ball_index
		global top_left_x
		global top_left_y
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.dx = random.randint(0,200)/200
		self.dy = random.randint(0,200)/200
		ball_index += 1
		self.index = ball_index

	def random_colors(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)

	#this function changes the balls' direction after collisions	
	def reverse_direction(self, factor):
		return (factor * -1)
	#this function chaecks the collisions between balls

	def add_ball(self, border):
		global ball_list
		random_radius = random.randint(10,20)
		new_ball = Ball(random_radius, "yellow", 1,1,1)
		new_ball.hideturtle()
		new_ball.penup()
		new_ball.goto(-300,0)
	 
		while True:
			x_1 = border.top_left_x + random_radius
			x_2 = (border.top_left_x + border.length) - random_radius
			y_1 = border.top_left_y - random_radius
			y_2 = (border.top_left_y - border.length) + random_radius
			random_x_pos = random.randint(x_1, x_2)
			random_y_pos = random.randint(y_2, y_1)
			print(str(random_x_pos)+ " "+ str(random_y_pos))
			new_ball.goto(random_x_pos, random_y_pos)
			#print(str(random_x_pos)+ " "+ str(random_y_pos))

			success = True
			for ball in (ball_list):
				if ball.ball_collide(border, new_ball):
					success = False
					break
			if success:
				ball_list.append(new_ball)
				new_ball.showturtle()
				new_ball.goto(random_x_pos, random_y_pos)
				break
	
	def ball_collide(self, border, other_ball):
		collide_dist1 = self.radius + other_ball.radius
		distance1 = math.sqrt (math.pow(self.xcor() - other_ball.xcor(),2) + math.pow(self.ycor() - other_ball.ycor(),2))
		if distance1 <collide_dist1:
			self.random_colors()
			other_ball.random_colors()
			#self.add_ball(border)
			
			return (True)
		return (False)

	#checks the y cordinates 
	def border_collide_X(self, border):
		if (self.xcor() - self.radius) <= border.top_left_x or \
			(self.xcor() + self.radius) >= (border.top_left_x + border.length):
			self.random_colors()
			return (True)
		return(False)
	#checks the x cordinates

	def border_collide_Y(self, border):
		if (self.ycor() - self.radius) <= border.top_left_y - border.length  or \
			(self.ycor() + self.radius) >= border.top_left_y:
			self.random_colors()
			return (True)
		return(False)


	def move_ball(self, border):
		global ball_list
		#- this line makes the ball move in a cross
		self.goto(self.xcor()+self.dx,self.ycor()+self.dy) 
		for ball in (ball_list):
			if self.index != ball.index:
				if self.ball_collide(border, ball):
					self.dx = self.reverse_direction(self.dx)
					self.dy = self.reverse_direction(self.dy)
		# check borders
		if self.border_collide_X(border):
			self.dx = self.reverse_direction(self.dx)
		if self.border_collide_Y(border):
			self.dy = self.reverse_direction(self.dy)
	
#object border	
Border = SquaredBorder(-250, 250, 500)
Border.make_square()
# Place Balls in initial locations
ball1 = Ball(40,"green",1,1,1)
ball1.penup()
ball1.goto(-40,-80)
ball2 = Ball(25,"black",2,1,1)
ball2.penup()
ball2.goto(-100,200)

#this function creates balls
#def make_balls():
random_radius = random.randint(10,50)
ball3 = Ball(random_radius,"red",2,1,1)
ball3.penup()



ball_list.append(ball1)
ball_list.append(ball2)
ball_list.append(ball3)
# Move balls around
while True: 
	for ball in (ball_list):
		ball.move_ball(Border)
	turtle.update()
	
turtle.mainloop()