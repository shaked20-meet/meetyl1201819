from turtle import *
import turtle
import random
import math

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
	    
		
		
	def move_balls(self):
		right_edge = 250
		left_edge = -250
		up_edge = 500
		down_edge = -500
		
		for i in range(30):
			self.penup()
			self.goto(self.xcor()+self.dx,self.ycor()+self.dy)

		
		
ball1 = Ball(100,"green",12,12,12)
ball1.move_balls()
ball2 = Ball(50,"black",10,10,10)
ball2.move_balls()
turtle.mainloop()