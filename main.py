import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guesses_list = []
score = 0
while len(guesses_list) < 50:
    answer_state = screen.textinput(f"{score}/50", "Guess Another State").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guesses_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x) , int(state_data.y))
        guesses_list.append(answer_state)
        t.write(answer_state)
        score += 1










