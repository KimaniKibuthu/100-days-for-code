from turtle import Turtle, Screen
import random

turtle_object = Turtle()
screen = Screen()
screen.colormode(255)


def draw_square(length):
    i = 0
    turtle_object.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    while i < 4:
        turtle_object.forward(length)
        turtle_object.right(90)
        i += 1


def draw_dashed_line():
    i = 0
    while i < 5:
        turtle_object.pendown()
        turtle_object.forward(10)
        turtle_object.penup()
        turtle_object.forward(10)
        i += 1


def draw_shapes_refactored(length, num_sides):
    i = 0
    turtle_object.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    while i < num_sides:
        turtle_object.forward(length)
        turtle_object.right(360 / num_sides)
        i += 1


def random_walk(distance, iterations):
    i = 0
    turtle_object.pensize(15)
    angles = [0, 90, 180, 270]
    while i < iterations:
        turtle_object.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle_object.setheading(random.choice(angles))
        turtle_object.forward(distance)
        i += 1


def spirograph(size_of_gap):
    turtle_object.speed('fastest')
    for i in range(int((360/size_of_gap) + 1)):
        turtle_object.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle_object.circle(100)
        turtle_object.left(size_of_gap)


screen.exitonclick()
