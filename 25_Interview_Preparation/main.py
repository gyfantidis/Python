import math
from tkinter import *
from data import interview_questions, phrases
import random

# ---------------------------- CONSTANTS ------------------------------- #

SOFT_BLUE = "#068FFF"
HARD_BLUE = "#4E4FEB"
WHITE = "#EEEEEE"
FONT_NAME = "Ariel"
reps = 0
timer = None


# ---------------------------- get start -------------------#
def get_start():
    check_label.config(text="")
    get_started.grid_forget()
    question_label.grid_forget()
    begin_button.grid(column=1, row=9)
    answer_sec_entry.grid(column=1, row=3)
    prepare_sec_entry.grid(column=1, row=5)
    questions_number_entry.grid(column=1, row=7)
    answer_sec_entry_label.grid(column=1, row=2)
    prepare_sec_entry_label.grid(column=1, row=4)
    questions_number_entry_label.grid(column=1, row=6)
    empty_label.grid(column=1, row=8)


# ---------------------------- begin interview ------------------------------- #

def begin_interview():
    answer_sec_entry.grid_forget()
    prepare_sec_entry.grid_forget()
    questions_number_entry.grid_forget()
    answer_sec_entry_label.grid_forget()
    prepare_sec_entry_label.grid_forget()
    questions_number_entry_label.grid_forget()
    empty_label.grid_forget()
    next_button.grid(column=2, row=0)
    end_button.grid(column=0, row=0)
    time_label.grid(column=1, row=3)
    category_label.grid(column=1, row=1)
    question_label.grid(column=1, row=2)
    begin_button.grid_forget()
    next_question()


# ------------------------- button next question---------------#
def next_btn():
    window.after_cancel(timer)
    time_label.config(text="00:00")
    next_question()


# -------------------------- next question function ---------------#

def next_question():
    global reps
    reps = reps + 1
    question = random.choice(interview_questions)
    answer_sec = int(answer_sec_entry.get())
    short_break_sec = int(prepare_sec_entry.get())
    number_of_questions = int(questions_number_entry.get())

    left_questions = number_of_questions - (reps / 2)

    if left_questions > 0:
        if reps % 2 == 0:
            category_label.config(text="")
            count_down(short_break_sec)
            question_label.config(text=random.choice(phrases), fg=SOFT_BLUE)

        else:
            count_down(answer_sec)
            question_label.config(text=f"{question['question']}", fg=HARD_BLUE)
            category_label.config(text=f"Category: {question['category']}")
            print(f"{question['question']}")

    else:
        end_interview()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    time_label.config(text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        next_question()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔️"

        if mark:
            check_label.config(text=f"{mark} / {int(questions_number_entry.get())}")
        else:
            check_label.config(text=f"{int(questions_number_entry.get())}")


# ------------------------ end interview button ---------------------#
def end_interview():
    window.after_cancel(timer)
    time_label.config(text="00:00")
    question_label.config(text="Interview Completed. \nClick Begin Interview for a New Session!")
    category_label.config(text="")
    next_button.grid_forget()
    end_button.grid_forget()
    time_label.grid_forget()
    get_started.grid(column=1, row=5)
    global reps
    reps = 0


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Interview Preparation")
window.config(padx=100, pady=50, bg=WHITE)

# ---------------- LABELS ---------------------#

category_label = Label(text="", bg=WHITE, fg="black", font=(FONT_NAME, 20, "bold"))

question_label = Label(text="Get Ready for Your Interview", bg=WHITE, fg=HARD_BLUE, font=(FONT_NAME, 40, "bold"))
question_label.grid(column=1, row=2)

time_label = Label(text="00:00", bg=WHITE, fg="red", font=(FONT_NAME, 35, "bold"))

check_label = Label(bg=WHITE, fg=HARD_BLUE, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=6)

# ------------------ BUTTONS ----------------------#

get_started = Button(bg=SOFT_BLUE, fg=WHITE, font=(FONT_NAME, 35, "bold"), text="Get Started",
                     highlightthickness=0,
                     command=get_start)
get_started.grid(column=1, row=5)

begin_button = Button(bg=SOFT_BLUE, fg=WHITE, font=(FONT_NAME, 35, "bold"), text="Begin Interview",
                      highlightthickness=0,
                      command=begin_interview)

next_button = Button(text="Next \nQuestion", font=(FONT_NAME, 35, "bold"), fg=SOFT_BLUE, highlightthickness=0,
                     command=next_btn)
end_button = Button(text="Finish \nInterview", font=(FONT_NAME, 35, "bold"), fg=SOFT_BLUE, highlightthickness=0,
                    command=end_interview)

# ------------------ ENTRYS --------------------------#

answer_sec_entry = Entry(width=60)
prepare_sec_entry = Entry(width=60)
questions_number_entry = Entry(width=60)
answer_sec_entry_label = Label(width=60, text="Answer Time (sec):")
prepare_sec_entry_label = Label(width=60, text="Prepare Time (sec):")
questions_number_entry_label = Label(width=60, text="Number of Questions:")
empty_label = Label(width=60, text="")

# -------------------- CANVAS -------------------------------#

canvas = Canvas(width=500, height=500, bg=WHITE, highlightthickness=0)
interview_img = PhotoImage(file="images/interview2.png")
canvas.create_image(250, 250, image=interview_img)
canvas.grid(column=1, row=0)

window.mainloop()
