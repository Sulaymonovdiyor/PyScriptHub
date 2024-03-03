import turtle
t = turtle.Pen()
turtle.bgcolor("grey")
x = 0
for i in range(300):
    t.pencolor("pink")
    x += .1
    t.width(x)
    t.forward(i)
    t.right(57)
