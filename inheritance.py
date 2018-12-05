#####################Exercise 1!###########

import turtle
from turtle import Turtle
turtle.colormode(255)
import random
'''
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
'''
##########Exercise 2#################
#turtle.hideturtle()
turtle.pensize(3)
class hexagon(Turtle):
	def __init__ (self):
		Turtle.__init__(self)
		self.shape = hexagon
	def make_hexagon(self):
		turtle.penup()
		turtle.goto(-300,0)
		turtle.pendown()
		turtle.begin_poly()
		for i in range(6):
			turtle.forward(100)
			turtle.right(60)
		turtle.end_poly()
		
		
		turtle.register_shape("hexagon",turtle.get_poly())
	def more_hexagons(self):
		turtle.speed(500)
		for i in range (100):
			def random_colors_hexagons():
				r= random.randint(0,255)
				g= random.randint(0,255)
				b= random.randint(0,255)
				self.color(r,g,b)
				turtle.pencolor(r,g,b)
			random_colors_hexagons()

			turtle.penup()
			turtle.forward(5)
			turtle.pendown()
			for m in range(6):
				turtle.forward(100)
				turtle.right(60)
s = hexagon()
s.make_hexagon()
s.more_hexagons()
turtle.mainloop()