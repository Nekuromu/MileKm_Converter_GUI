from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button

def button_clicked():
    print("I got clicked")
    my_label.config(text=my_entry.get())


my_button = Button(text="Click Me", command=button_clicked)
my_button.pack()

# Entry

my_entry = Entry(width=10)
my_entry.insert(END, "Email")
my_entry.pack()

# Text
my_text = Text(height=5, width=15)
my_text.focus()
my_text.insert(END, "Example of multi-line text entry.")
print(my_text.get("1.0", END))
my_text.pack()


# Spinbox
def spinbox_used():
    print(my_spinbox.get())


my_spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
my_spinbox.pack()


# Scale
def scale_used(value):
    print(value)


my_scale = Scale(from_=0, to=100, command=scale_used)
my_scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
my_checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
my_checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
my_radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
my_radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
my_radiobutton1.pack()
my_radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(my_listbox.get(my_listbox.curselection()))


my_listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    my_listbox.insert(fruits.index(item), item)
my_listbox.bind("<<ListboxSelect>>", listbox_used)
my_listbox.pack()

window.mainloop()
