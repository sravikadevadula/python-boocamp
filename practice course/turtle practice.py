import turtle

display=turtle.Screen()
turtle = turtle.Turtle()
turtle.color("purple")
turtle.pensize(5)
turtle.shape("arrow")
turtle.speed(3)

def rectangle(edge=100):
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)

def triangle(edge=15):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)

rectangle()
#for ears:
turtle.circle(30)
turtle.circle(20)
turtle.forward(100)
turtle.circle(30)
turtle.circle(20)
#for eyes:
turtle.penup()
turtle.setpos(20,-30)
turtle.pendown()
turtle.circle(10)
turtle.penup()
turtle.setpos(80,-30)
turtle.pendown()
turtle.circle(10)
#for nose:
turtle.penup()
turtle.setpos(42,-50)
turtle.pendown()
triangle()
#for mouth:
turtle.penup()
turtle.setpos(30,-70)
turtle.pendown()
turtle.right(90)
turtle.circle(20,180)
turtle.hideturtle()

display.mainloop()
