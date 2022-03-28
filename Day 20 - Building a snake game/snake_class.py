from turtle import Turtle, Screen

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

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

        self.segments[0].forward(DISTANCE)

    def up(self):
        self.segments[0].left(90)
        self.move()
    
    def down(self):
        self.segments[0].right(90)
        self.move()
    
    def lefty(self):
        self.segments[0].left(90)
        self.move()
    
    def righty(self):
        self.segments[0].right(90)
        self.move()
