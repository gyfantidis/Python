from tkinter import *

import pandas
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------ Data ------------------------#

current_card={}
to_learn={}
# Read the CSV file

try:
    data=read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=read_csv("data/english_greek.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="Greek", fill="black")
    canvas.itemconfig(word_text, text=current_card["Greek"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def is_know():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()





# ---------------------- UI SETUP -------------------#

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"])
    canvas.itemconfig(card_bg, image=card_back_image)


window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# --- Canvas----#

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# ---Buttons---#

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_know)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
