"""A house with 3 windows and a door."""

__author__ = "730431294"

from turtle import Turtle, colormode, done

colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    house: Turtle = Turtle()
    house.color("red")
    house.begin_fill()
    draw_triangle(house, -50, 0, 100)
    house.end_fill()
    draw_window(house, -35, -10, 10)
    draw_window(house, -5, -10, 10)
    draw_window(house, 25, -10, 10)
    house.color("green")
    draw_rectangle(house, -5, -100, 20, 10)
    draw_square(house, -50, 0, 100)
    house.hideturtle()
    done()
    

def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width with top-left corner located at (x, y)."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1


def draw_line(a_turtle: Turtle, x: float, y: float, length: float, direction: float) -> None:
    """Draw a line starting from (x,y) with length l and direction d."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(direction)
    a_turtle.pendown()
    a_turtle.forward(length)


def draw_triangle(a_turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draw a triangle with side length l and bottom-left point located at (x, y)."""
    a_turtle.penup()
    a_turtle.setheading(0.0)
    a_turtle.goto(x, y)
    a_turtle.pendown()
    i: int = 0
    while i < 3:
        a_turtle.forward(length)
        a_turtle.left(120)
        i = i + 1


def draw_rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw a rectangular with given width and lenth and a starting point (x, y)."""
    a_turtle.penup()
    a_turtle.setheading(0.0)
    a_turtle.goto(x, y)
    a_turtle.pendown()
    i: int = 0
    while i < 2:
        a_turtle.forward(width)
        a_turtle.left(90)
        a_turtle.forward(length)
        a_turtle.left(90)
        i = i + 1


def draw_window(a_turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draw a window using draw_square and draw_line functions."""
    draw_square(a_turtle, x, y, length)
    x_line1: float = x
    x_line2: float = x + 0.5 * length
    y_line1: float = y - 0.5 * length
    y_line2: float = y - length
    draw_line(a_turtle, x_line1, y_line1, length, 0)
    draw_line(a_turtle, x_line2, y_line2, length, 90)
    

if __name__ == "__main__":
    main()