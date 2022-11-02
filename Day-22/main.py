from turtle import Screen, Turtle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)





game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    if ball().ycor >300 or  if ball().ycor < 300:
        ball.bounce()
    

    if ball.distance(r_paddle) <50 and ball.xcor() >340 or ball.distance(l_paddel )<:

    #detect right paddle miiises

        
screen.exitonclick()
