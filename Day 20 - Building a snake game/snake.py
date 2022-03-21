from turtle import Turtle, Screen
import time



screen = Screen()
screen.bgcolor('black')
screen.title('Snake Xenzia')
screen.tracer(0)

segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    segment = Turtle('square')
    segment.color('white')
    segment.penup()
    segment.goto(position)
    segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment_number in range(len(segments)-1, 0, -1):
        new_x = segments[segment_number-1].xcor()
        new_y = segments[segment_number-1].ycor()
        segments[segment_number].goto(new_x, new_y)

    segments[0].forward(20)

    

    


    

screen.exitonclick()



# def run():
#     is_continue = True
#     while is_continue:
#         # Build turtles
#         # Create food randomly
#         # Move continously
