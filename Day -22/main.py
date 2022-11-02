from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
