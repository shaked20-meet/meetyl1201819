import turtle
from turtle import Turtle
import random 
import math

turtle.hideturtle()
turtle.register_shape("CharacterLeft.gif")
turtle.shape("CharacterLeft.gif")
turtle.pensize(100)
turtle.pu()
turtle.goto(-450,-200)
turtle.showturtle()
def move_Right():
	x=turtle.pos()[0]
	y=turtle.pos()[1]
	turtle.goto(x+5,y)
def move_Left():
	x=turtle.pos()[0]
	y=turtle.pos()[1]
	turtle.goto(x-5,y)
def move_Up():
	x=turtle.pos()[0]
	y=turtle.pos()[1]
	turtle.goto(x,y+30)
	turtle.goto(x,y)
def move_Down():
	x=turtle.pos()[0]
	y=turtle.pos()[1]
	turtle.goto(x,y-5)

OBSTICLES_LIST = []
OBSTICLES_X_POS_LIST = []
OBSTICLES_Y_POS_LIST = []
OBSTICLES_MAX_NUMBER = 5
class obsitcles(Turtle):
	def __init__(self,x,y,dx):
		Turtle.__init__(self)
		self.pu()
		self.x = x
		self.y = y
		self.dx = x
		self.shape("square")
		self.hideturtle()
		self.goto(self.x,self.y)
		self.showturtle()

	def move(self):
		
		x=self.pos()[0]
		y=self.pos()[1]
		self.goto(x-2,y)
		self.check_collision(OBSTICLES_LIST)

	def make_obsticles(self, OBSTICLES_LIST):
		global OBSTICLES_MAX_NUMBER
		self.y = random.randint(-500,500)
		new_obsticle = obsitcles(300,self.y,5)
		OBSTICLES_LIST.append(new_obsticle)
		OBSTICLES_X_POS_LIST.append(new_obsticle.xcor())
		OBSTICLES_Y_POS_LIST.append(new_obsticle.ycor())
	def check_collision(self, OBSTICLES_LIST):	
		for i in (OBSTICLES_LIST):
			if self.pos() in i.pos():
				print("you hit me!") 

obsticle_1 = obsitcles(500,300,5)

s = turtle.getscreen()

while True:	
	obsticle_1.move()
	for obsticle in (OBSTICLES_LIST):
		obsticle.move()
	while len(OBSTICLES_LIST) < OBSTICLES_MAX_NUMBER:
		obsticle_1.make_obsticles(OBSTICLES_LIST)
	s.onkeypress(move_Right,'Right')
	s.onkeypress(move_Left,'Left')
	s.onkeypress(move_Up, 'Up')
	s.onkeypress(move_Down, 'Down')
	s.listen()





turtle.mainloop()