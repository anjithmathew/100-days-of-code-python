from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move =10
        self.ymove =10
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.move(new_x, new_y)
    
    def bounceY(self):
        new_y = self.ymove *=-1
    
    def bounceX(self):
        new_X = self.Xmove *=-1

