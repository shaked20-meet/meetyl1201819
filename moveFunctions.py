import startButtons
from startButtons import *
def moveRight():
	Princess.goto(Princess.pos()[0]+20,Princess.pos()[1])
def moveLeft():
	Princess.goto(Princess.pos()[0]-20,Princess.pos()[1])
def moveUp():
	Princess.goto(Princess.pos()[0],Princess.pos()[1]+20)
def moveDown():
	Princess.goto(Princess.pos()[0],Princess.pos()[1]-20)
