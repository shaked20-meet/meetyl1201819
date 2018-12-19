import turtle
from turtle import *
turtle.colormode(255)
import random
import math
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
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.dx =dx
		self.dy = dy
	def random_colors(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)

	#this function changes the balls' direction after collisions	
	def reverse_direction(self, factor):
		return (factor * -1)
	#this function chaecks the collisions between balls
	def ball_collide(self, other_ball,ball3):
		collide_dist1 = self.radius + other_ball.radius
		collide_dist2 = self.radius + ball3.radius
		collide_dist3 = ball3.radius + other_ball.radius
		distance1 = math.sqrt (math.pow(self.xcor() - other_ball.xcor(),2) + math.pow(self.ycor() - other_ball.ycor(),2))
		distance2 = math.sqrt (math.pow(self.xcor() - ball3.xcor(),2) + math.pow(self.ycor() - ball3.ycor(),2))
		distance3 = math.sqrt (math.pow(ball3.xcor() - other_ball.xcor(),2) + math.pow(ball3.ycor() - other_ball.ycor(),2))
		if distance1 <= collide_dist1:
			self.random_colors()
			other_ball.random_colors()
			return (True)
		if distance2<= collide_dist2:
			self.random_colors()
			ball3.random_colors()
			return (True)
		if distance3 <= collide_dist3:
			other_ball.random_colors()
			ball3.random_colors()
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


	def move_ball(self, border, other_ball, ball3):
		#- this line makes the ball move in a cross
		self.goto(self.xcor()+self.dx,self.ycor()+self.dy) 
		if self.ball_collide(other_ball,ball3):
			self.dx = self.reverse_direction(self.dx)
			self.dy = self.reverse_direction(self.dy)
		if self.border_collide_X(border):
			self.dx = self.reverse_direction(self.dx)
		if self.border_collide_Y(border):
			self.dy = self.reverse_direction(self.dy)
	
#object border	
Border = SquaredBorder(-250, 250, 500)
Border.make_square()
# Place Balls in initial locations
ball1 = Ball(40,"green",1,1,3)
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

	


#this function duplicates the smaller balls to random positions
def duplication():
	#ball_list = [ball1, ball2,ball3]
	if ball1.ball_collide(ball2, ball3):
		random_radius = random.randint(10,50)
		ball = Ball(random_radius,"yellow",2,1,1)
		ball.penup()
		ball.goto(80,90)
		ball.move_ball(ball1,ball2,ball3)
duplication()
# Move balls around
while True:
	ball1.move_ball(Border, ball2, ball3)
	ball2.move_ball(Border, ball1, ball3)
	ball3.move_ball(Border, ball2, ball1)
turtle.mainloop()