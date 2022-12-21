from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    print("I got clicked")
    my_label.config(text=my_entry.get())


# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
my_button = Button(text="Click Me", command=button_clicked)
my_button2 = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)
my_button2.grid(column=2, row=0)

# Entry
my_entry = Entry(width=10)
my_entry.insert(END, "Email")
my_entry.grid(column=3, row=2)

window.mainloop()