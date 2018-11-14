import turtle
from turtle import Turtle
turtle.colormode(255)
import random
class Square(Turtle):
	def __init__(self, shapesize, shape, color):
		Turtle.__init__(self)
		self.shapesize(shapesize)
		self.shape(shape)
		self.color(r+b+g)
		
	def random_color1(self):
		r= random.randint(0,255)
		g= random.randint(0,255)
		b= random.randint(0,255)
		self.color(r+b+g)
		
s = Square(8,"square")
s.random_color1()
turtle.mainloop()