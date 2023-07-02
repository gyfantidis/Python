from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
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

    new_data = {website: {
        "username": username,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oooops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nUsername: {username} \nPassword: {password} \nIs it ok to sava?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # data_file.write(f"\n{website} | {username} | {password}")
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data,data_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------- find_password -------------------------------#

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="No Data File Found")
    else:
        if website in data:
            website_details = data[website]
            messagebox.showinfo(title=website, message=f"These are the passwords for the {website}: \nUsername: {website_details['username']} \nPassword: {website_details['password']} ")
        else:
            messagebox.showinfo(title="No data", message="No details for the website exists.")



# ---------------------------- UI SETUP ------------------------------- #

########### WINDOW ##############################

window = Tk()
window.title("Password Manager")
window.config(padx=22, pady=22)

########## CANVAS #############################

canvas = Canvas(width=222, height=222, highlightthickness=0)
key_img = PhotoImage(file="logo.png")
canvas.create_image(111, 111, image=key_img)
canvas.grid(column=1, row=0)

################### LABELS #####################

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

################# ENTRYS ##########################

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()

username_entry = Entry(width=70)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
username_entry.insert(0, "example@email.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, sticky="w")

############# BUTTONS ###############

generate_password_button = Button(width=25, text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w")

add_button = Button(width=60, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

search_button = Button(width=25, text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="w")

window.mainloop()
