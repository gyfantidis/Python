import tkinter
from playground import add

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()






add(1,2,3,-4,2,1,2,3,4)











window.mainloop()
