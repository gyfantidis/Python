from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------ Data ------------------------#


# Read the CSV file
data = read_csv("data/english_greek.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=current_card["English"])








# ---------------------- UI SETUP -------------------#

window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# --- Canvas----#

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_photo = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=bg_photo)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# ---Buttons---#

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
