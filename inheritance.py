import turtle
from turtle import Turtle
turtle.colormode(255)
import random
class Square(Turtle):
	def __init__(self, shapesize, shape):
		Turtle.__init__(self)
		self.shapesize(shapesize)
		self.shape(shape)
		
		
	def random_color1(self):
		r= random.randint(0,255)
		g= random.randint(0,255)
		b= random.randint(0,255)
		self.color(r,g,b)
		

s = Square(8,"square")
s.random_color1()
turtle.mainloop()

