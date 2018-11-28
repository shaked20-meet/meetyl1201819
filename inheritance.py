#####################Exercise 1!###########
'''
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
'''
##########Exercise 2#################
import turtle
class hexagon(Turtle):
	def __init__(self, shapesize):
		Turtle.__init__(self)
		self.shapesize(shapesize)
	def draw_hexagon(self):
		turtle.begin_poly()
		for i in range (6):
			turtle.forward(10)
			turtle.left(120)
		turtle.end_poly()

s = hexagon(5)
hexagon.draw_hexagon()
		

turtle.mainloop()



