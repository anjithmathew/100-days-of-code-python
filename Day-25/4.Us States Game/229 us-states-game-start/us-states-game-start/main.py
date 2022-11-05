from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()

screen.title("U S State Game")
image = "/home/anjithmathew/Documents/1.Python/100-days-of-code-python/Day-25/4.Us States Game/229 us-states-game-start/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


text_input = screen.textinput("Guess The State", "what another state name")

with open("/home/anjithmathew/Documents/1.Python/100-days-of-code-python/Day-25/4.Us States Game/229 us-states-game-start/us-states-game-start/50_states.csv") as file:
    
screen.exitonclick()
