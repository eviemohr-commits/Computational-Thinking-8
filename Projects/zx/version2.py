import turtle 

t = turtle.Turtle()
t.penup()
t.goto(-50, -50)
t.color("red")
t.pendown()

for i in range (6):
    t.forward(50)
    t.left(60)

turtle.exitonclick()