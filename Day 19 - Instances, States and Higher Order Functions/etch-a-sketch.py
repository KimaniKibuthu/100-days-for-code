from turtle import Turtle, Screen

etcher = Turtle()
screen = Screen()

def move_forwards():
    etcher.forward(1)

def move_backwards():
    etcher.backward(1)

def move_clockwise():
    etcher.right(10)
    etcher.forward(10)

def move_counter_clockwise():
    etcher.left(10)
    etcher.forward(10)

def clear_drawing():
    etcher.clear()

screen.listen()
etcher.onclick()