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
square(90, -250, -200, 100, "red")
# Dashas figures (2)
q.speed(3)
isosceles_triangle(90, -300, 100, 100, 141.4, "light blue")
isosceles_triangle(270,-229.29, 170.71, 100, 141.4, "light grey")
isosceles_triangle(180, -229.29, 170.71, 141.4, 200, "white")
isosceles_triangle(270, -87.89, 170.71, 100, 141.4, "light grey")
q.goto( -150, 300)
q.pendown()
q.begin_fill()
q.fillcolor("yellow")
q.circle(35)
q.end_fill()

square(90, 200, 100, 100, "brown")
isosceles_triangle(90, 76.75, 200, 100, 141.4, "dark green")
square(90, 175, 125, 50, "light blue")
q.goto(147.46, 270.71)
q.pendown()
q.forward(25)
isosceles_triangle(225, 197.46, 290.71, 50, 70.7, "red")