from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
leo.goto(0, 0)
colormode(255)
leo.setheading(90.0)
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

done()
