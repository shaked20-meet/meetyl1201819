import turtle
from turtle import *
import math

global screen_height
global screen_width
screen_width = 250
screen_height = 250 
#creates the balls
class Ball(Turtle):
	def __init__(self, x, y, dx, dy, radius, color):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.penup()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.radius = radius
		self.shapesize(radius/10)
		self.color(color)
		self.penup()
#moves balls around 
	def move_ball (self, screen_width, screen_height):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		
		right_side_ball = new_x + self.radius
		left_side_ball = new_x - self.radius
		top_side_ball = new_y + self.radius
		bottom_side_ball = new_y - self.radius 

		self.goto(new_x, new_y)
		if  right_side_ball > screen_width:
			self.dx = -1 * self.dx
			self.goto(new_x,new_y)
		if left_side_ball < -screen_width:
			self.dx = -1 * self.dx 
			self.goto(new_x,new_y)                  
		if top_side_ball > screen_height:
			self.dy = -1 * self.dy 
			self.goto(new_x,new_y)    
		if bottom_side_ball < -screen_height: 
			self.dy = -1 * self.dy 
			self.goto(new_x,new_y)       
