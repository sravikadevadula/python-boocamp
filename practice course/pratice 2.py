import turtle

display=turtle.Screen()
turtle = turtle.Turtle()
turtle.color("orange")
turtle.pensize(8)
turtle.shape("arrow")

def triangle(edge=100):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(60)

triangle()
triangle()
triangle()
triangle()
triangle()
triangle()

display.mainloop()