from turtle import Turtle, Screen  # importing turtle modules and screen module
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE =20
UP =90
DOWN =270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
         # doubts watch the turtorial once again (start=2,stop=0,step=-1)
        for seg_num in range(len(segments)-1, 0, -1):
                new_x =self.segments[seg_num -1 ].xcor()
                new_y =self.segments[seg_num -1 ].ycor()
                self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.segments[0].setheading(UP)
    
    
    def down(self):
        if self.head.heading() != UP:
            self.head.segments[0].setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.segments[0].setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.segments[0].setheading(RIGHT)
        
        
        