import turtle

q = turtle.Turtle()


# TODO 3 def 1 Lida - square, 2 Dasha - tr & par

# Dashas def
def isosceles_triangle(angle, x, y, a, b, color):
    q.penup()
    q.goto(x, y)
    q.pendown()
    q.setheading(angle)
    q.fillcolor(color)
    q.begin_fill()
    q.right(45)
    q.forward(a)
    q.right(90)
    q.forward(a)
    q.right(135)
    q.forward(b)
    q.end_fill()
    q.penup()


def parallelogram(angle0, x, y, angle1, angle2, a, b, color):
    q.penup()
    q.goto(x, y)
    q.pendown()
    q.setheading(angle0)
    q.fillcolor(color)
    q.begin_fill()
    q.right(angle1)
    q.forward(a)
    q.right(angle2)
    q.forward(b)
    q.right(angle1)
    q.forward(a)
    q.right(angle2)
    q.forward(b)
    q.end_fill()
    q.penup()


# Lidas def
def square(angle0, x, y, a, color):
    q.penup()
    q.goto(x, y)
    q.pendown()
    q.setheading(angle0)
    q.fillcolor(color)
    q.begin_fill()
    q.forward(a)
    q.left(angle0)
    q.forward(a)
    q.left(angle0)
    q.forward(a)
    q.left(angle0)
    q.forward(a)
    q.left(angle0)
    q.end_fill()
    q.penup()


# Lida's figures (2)
square(90, -150, -150, 100, "red")
# Dashas figures (2)
isosceles_triangle(90, -300, 300, 100, 141.4, "yellow")
parallelogram(90, -200, 200, 60, 120, 100, 50, "green")
