import turtle

t = turtle.Turtle()

turtle.bgcolor("red")
turtle.pensize(2)
turtle.speed(0)

while (True):

    for i in range(6):
        for colors in ["white"]:
            turtle.color(colors)
            turtle.circle(300)
            turtle.left(100)

turtle.hidrturtle()
turtle.maintoop()
