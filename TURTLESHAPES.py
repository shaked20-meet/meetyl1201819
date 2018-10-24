#everything is inside a comment so I will be able to work on the same file ####################
#first task, star shape######
#import turtle
#turtle.goto(100,0)
#for i in range(5):
	#turtle.right(216)
	#turtle.forward(150)
#turtle.mainloop()
#######second task, arrow-like shape####
'''
import turtle
turtle.goto(100,0)
turtle.begin_fill()
turtle.right(90)
turtle.forward(50)
turtle.left(320)
turtle.forward(75)
turtle.left(260)
turtle.forward(75)
turtle.left(320)
turtle.forward(50)
turtle.mainloop()
'''
##########third task#################
'''
import turtle
turtle.addshape("avocado.gif")
turtle.shape("avocado.gif")

turtle.goto(100,100)
turtle.mainloop()
'''
###########forth task################3
'''
import turtle
def strange_shape():
	turtle.left(30)
	turtle.speed(0)
	turtle.forward(150)
	turtle.left(300)
	turtle.forward(75)
	turtle.right(100)
	turtle.forward(70)
for i in range (3000):
	strange_shape()
	turtle.penup()
	turtle.home()
	turtle.pendown()
	turtle.left(i + 30)
turtle.mainloop()
'''