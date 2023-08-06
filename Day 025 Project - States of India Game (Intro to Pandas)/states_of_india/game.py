import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India States Game")
image_path = "india.gif"
#image_path2 = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)

data = pd.read_csv("states.csv")
all_states = data.state.to_list()
all_states_len = len(all_states)
guessed_state = []

while len(guessed_state) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{all_states_len} States Correct",
                                    prompt="What's another state's name?")

    answer_state = answer_state.upper()
    #print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

#turtle.exitonclick()


#Code used to find the co-ordinates of the states
#def get_mouse_click_coor(x, y):
    #print(x,y)

#turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop()