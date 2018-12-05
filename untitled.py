import turtle
from turtle import *
import random

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
ball1 = Ball(100,"green",20)
ball2 = Ball(50,"black",10)
turtle.mainloop()