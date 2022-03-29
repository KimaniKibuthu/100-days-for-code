from turtle import Turtle, Screen

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFTY = 180
RIGHTY = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
    
    def move(self):
        for segment_number in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment_number-1].xcor()
            new_y = self.segments[segment_number-1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

        self.head.forward(DISTANCE)

    def righty(self):
        if self.head.heading() != LEFTY:
            self.head.setheading(RIGHTY)
            
    
    def lefty(self):
        if self.head.heading() != RIGHTY:
            self.head.setheading(LEFTY)
            
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
