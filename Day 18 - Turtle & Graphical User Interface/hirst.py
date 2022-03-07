import colorgram
import random
from turtle import Turtle, Screen

colors = colorgram.extract('hirst.jpg', -1)
list_of_colors = [tuple(item.rgb) for item in colors]

turtle_neck = Turtle()
screen = Screen()
screen.colormode(255)


# Create painting
def painter():
    i = 0
    j = 0
    while j < 10:
        while i < 10:
            turtle_neck.pendown()
            turtle_neck.dot(20, random.choice(list_of_colors))
            turtle_neck.penup()
            turtle_neck.forward(50)

            i += 1
        turtle_neck.penup()
        turtle_neck.home()
        turtle_neck.setheading(90)
        turtle_neck.penup()
        j += 1
        turtle_neck.forward(50 * j)
        turtle_neck.pendown()
        turtle_neck.setheading(0)
        i = 0



painter()

screen.exitonclick()
