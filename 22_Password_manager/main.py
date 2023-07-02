from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def genetate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is: {password}")

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    print("Password saved!")
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oooops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nUsername: {username} \nPassword: {password} \nIs it ok to sava?")

        if is_ok:
            with open("file.txt", "a") as data_file:
                data_file.write(f"\n{website} | {username} | {password}")
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)
                data_file.close()


# ---------------------------- UI SETUP ------------------------------- #

########### WINDOW ##############################

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

########## CANVAS #############################

canvas = Canvas(width=400, height=400, highlightthickness=0)
key_img = PhotoImage(file="logo.png")
canvas.create_image(200, 200, image=key_img)
canvas.grid(column=1, row=0)

################### LABELS #####################

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

################# ENTRYS ##########################

website_entry = Entry(width=70)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=70)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "example@email.com")

password_entry = Entry(width=40)
password_entry.grid(column=1, row=3)

############# BUTTONS ###############

generate_password_button = Button(text="Generate Password", command=genetate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(width=60, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
