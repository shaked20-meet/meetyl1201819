import turtle
from turtle import *
import math


#creates the balls
class Ball(Turtle):
	def __init__(self, x, y, dx, dy, radius):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.screen_width = 250
		self.screen_hight = 250
		self.shape("circle")
		self.radius = radius
		self.shapesize(radius/10)
		self.color("red")
		turtle.setup(self.screen_width, self.screen_hight)
#moves balls around 
	def move_ball (self, screen_width, screen_hight):
		#turtle.screensize(screen_width, screen_hight)
		self.penup()
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		
		right_side_ball = new_x + self.radius
		left_side_ball = new_x - self.radius
		top_side_ball = new_y + self.radius
		bottom_side_ball = new_y - self.radius 

		self.goto(new_x, new_y)
		if  right_side_ball >= self.screen_hight:
			self.dx = -1 * self.dx 
			self.dy = -1 * self.dy
		if left_side_ball <= self.screen_hight:
			self.dx = -1 * self.dx 
			self.dy = -1 * self.dy                   
		if top_side_ball >= self.screen_width:
			self.dx = -1 * self.dx 
			self.dy = -1 * self.dy     
		if bottom_side_ball <= self.screen_width:
			self.dx = -1 * self.dx 
			self.dy = -1 * self.dy        

ball1 = Ball(0,0,1,1,10)

while True:

	ball1.move_ball(200,500)
 
turtle.mainloop()