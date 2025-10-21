# ###############################################
# ### SETUP ###
import turtle
turtle.Screen().bgcolor("pink")
# these are the colors in my code
t=turtle.Turtle()
t.speed(10)
# ###############################################
#this starts the drawing
t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("pink")
t.pendown()
# I love the shape
colors = ["pink", "blue", "purple"]
for i in range(400):
    t.color( colors[i % 3])
    t.forward(200)
    t.left(100)
    t.forward(150)
    #the speed was very good