from tkinter import *

FONT = ("Arial", 24, "bold")


def button_clicked():
    print("Converted")
    res = float(miles_to_convert.get()) * (1.609)
    result["text"] = f"{res}"


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

# Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)

result = Label(text="0", font=FONT)
result.grid(column=1, row=1)

# Button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry

miles_to_convert = Entry(width=10)
miles_to_convert.grid(column=1, row=0)

window.mainloop()
