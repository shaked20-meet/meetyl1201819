import turtle
import time
from turtle import *
turtle.shape("circle")

turtle.bgpic("frame.gif")
#turtle.bgpic("kingdom.gif")
player = Turtle()
player.hideturtle()
turtle.register_shape("story_player.gif")
player.shape("story_player.gif")

prince = Turtle()
prince.hideturtle()
turtle.register_shape("prince.gif")
prince.shape("prince.gif")

wizard = Turtle()
wizard.hideturtle()
turtle.register_shape("wizard.gif")
wizard.shape("wizard.gif")
wizard.pu()
wizard.goto(100,-250)

speech = Turtle()
speech.hideturtle()
turtle.register_shape("speech.gif")
speech.shape("speech.gif")
speech.pu()



def intro(x,y):
	turtle.penup()
	turtle.hideturtle()
	turtle.write("Once upon a time, in a far away land,", align = ("center"), font = ("comic sans MS", 25, "bold"))
	time.sleep(4)
	turtle.clear()
	turtle.write("lived a princess and a prince.", align = ("center"), font = ("comic sans MS", 25, "bold"))
	time.sleep(4)
	characters_show()
	turtle.clear()
	turtle.write("One day, the dark queen came to the palace.", align = ("center"), font = ("comic sans MS", 25, "bold"))
	time.sleep(4)
	turtle.clear()
	turtle.write("She demanded to rule the kingdom, but the prince refused.", align = ("center"), font = ("comic sans MS", 20, "bold"))
	time.sleep(4)
	turtle.clear()
	turtle.write("She snnaped her fingers...", align = ("center"), font = ("comic sans MS", 25, "bold"))
	time.sleep(4)
	turtle.clear()
	turtle.bgcolor("black")
	turtle.color("white")
	player.hideturtle()
	prince.hideturtle()
	turtle.write("...and the palace went dark.", align = ("center"), font = ("comic sans MS", 25, "bold"))
	time.sleep(4)
	turtle.clear()
	turtle.bgcolor("white")
	turtle.color("black")
	player.showturtle()
	turtle.write("When the lights were back on, the prince was gone.", align = ("center"), font = ("comic sans MS", 25, "bold"))
	time.sleep(4)
	turtle.clear()
	speech.goto(player.xcor(), player.ycor() + 192)
	speech.showturtle()
	turtle.goto(speech.pos())
	turtle.write("I must find him!", align = ("center"), font = ("comic sans MS", 15, "bold"))
	time.sleep(4)
	turtle.clear()
	wizard.showturtle()
	speech.showturtle()
	speech.goto(100, wizard.ycor() + 183.5)
	turtle.goto(speech.pos())
	turtle.write("I will help you!", align = ("center"), font = ("comic sans MS", 15, "bold"))
	time.sleep(2.5)
	turtle.clear()
	turtle.write("ARE YOU READY?", align = ("center"), font = ("comic sans MS", 15, "bold"))
	time.sleep(4)
	turtle.clear()
	speech.goto(player.xcor(), player.ycor() + 192)
	turtle.goto(speech.pos())
	turtle.write("Yes!", align = ("center"), font = ("comic sans MS", 25, "bold"))
	time.sleep(4)
	turtle.clear()
	speech.hideturtle()
	

def characters_show():
	player.pu()
	player.goto(-200, -250)
	player.showturtle()

	prince.pu()
	prince.goto(-100, -250)
	prince.showturtle()




turtle.onclick(intro)




turtle.listen()
turtle.mainloop()