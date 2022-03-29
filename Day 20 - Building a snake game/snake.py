from turtle import Turtle, Screen
import time
from snake_class import Snake
from food import Food
from scoreboard import Score




screen = Screen()
screen.bgcolor('black')
screen.title('Snake Xenzia')
screen.tracer(0)

snake = Snake()
foody = Food()
scores = Score()

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
    
    # Detect collision with food
    if snake.head.distance(foody) < 15:
        foody.refresh()
        scores.keep_score()
 

screen.exitonclick()

