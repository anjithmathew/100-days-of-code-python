from turtle import Turtle, Screen #importing turtle modules and screen module
import time
#create class
screen = Screen()



#setting up width and bg color
screen.setup(600, 600)
screen.bgcolor("black")

#title of screen
screen.title(" My Snake Game")

#tracer is turned off   
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
# #snake body

# #tuples for positioning snakes
# starting_postions = [(0,0),(-20,0),(-40,0)]

# segments = []
# #we must store tree snakes into segments because to organise or both 3 snakes move its on

# for position in starting_postions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup() #we solved the problem of trail of lines
#     new_segment.goto(position)
#     segments.append(new_segment)


#continously happen ->> while loop

game_is_on = True

while game_is_on:
    #move segment loop through each of segments
    #our screen must refrest all the segments have been move forward
    screen.update()
    time.sleep(0.1)
    snake.move()

        #then we get a trail of line from the segments we have to remove
        #we see creation of individual pieces and move forward to those directions
        #we must fix the problem using tracer
        
        #our snake segments are not linked
        #or it will go diffrent ways
    # for seg_num in range(len(segments)-1,0,-1): #doubts watch the turtorial once again (start=2,stop=0,step=-1)
    #     new_x =segments[seg_num -1 ].xcor()
    #     new_y =segments[seg_num -1 ].ycor()
    #     segments[seg_num].goto(new_x,new_y)



screen.exitonclick()
