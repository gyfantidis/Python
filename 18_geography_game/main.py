import turtle
import pandas

# Screen and Image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Import Data from CSV
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
state_list = data["state"].to_list()
print(data_dict)

game_is_on = True
guess = 0

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    if state_list.index(answer_state):
        print(answer_state.lower())
    else:
        pass


    def get_mouse_click_coor(x, y):
        print(x, y)


    if guess >= 50:
        game_is_on = False
    turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
