from turtle import Turtle, Screen
import time
from snake_class import Snake



screen = Screen()
screen.bgcolor('black')
screen.title('Snake Xenzia')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.lefty, 'Left')
screen.onkey(snake.righty, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
 

screen.exitonclick()



# def run():
#     is_continue = True
#     while is_continue:
#         # Build turtles
#         # Create food randomly
#         # Move continously
