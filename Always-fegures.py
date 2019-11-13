import turtle
q = turtle.Turtle()

#TODO 3 def 1 Lida - square, 2 Dasha - tr & par

# Dashas def
def isosceles_triangle(angle, x, y, a, b, color)
    q.penup()
    q.goto(x, y)
    q.pendown()
    q.setheading(angle0)
    q.fillcolor(color)
    q.begin_fill()
    q.right(45)
    q.forward(a)
    q.right(90)
    q.forward(a)
    q.right(45)
    q.forward(b)
    q.end_fill()
    q.penup()

def parallelogram(angle0, angle1, angle2, x, y, a, b, color)
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

#Lidas def

#Lidas figures (2)

#Dashas figures (1)
