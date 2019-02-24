import turtle
turtle.shape("square")
turtle.resizemode("user")
turtle.shapesize(1, 4)

print(turtle.shapetransform())

######################################################
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/4
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
print(SCREEN_HEIGHT)


turtle.mainloop()

global OBSTICLES_LIST
		x = self.pos()[0]
		y = self.pos()[1]
		self.goto(x - self.dx, y)
		for obsticle in (OBSTICLES_LIST):
			if obsticle.xcor() < -(2 * SCREEN_WIDTH):
				OBSTICLES_LIST.remove(obsticle)
				obsticle.hideturtle()
				turtle.update()
