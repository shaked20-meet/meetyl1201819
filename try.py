import turtle
import math
'''
#turtle.circle(20,180)
turtle.left(90)
turtle.left(1)

turtle.forward(1)

turtle.circle(20,180)
'''
turtle.goto(2,2)

for i in range(10):
	x = i  
	y = math.pow(x,2)
	turtle.goto(x,y)
turtle.mainloop()