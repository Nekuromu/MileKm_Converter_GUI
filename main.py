from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

round_state = IntVar()


def button_pressed():
    if miles_entry.get() == '' or not miles_entry.get().isdigit():
        return
    km = float(miles_entry.get()) * 1.60934
    if round_state.get() == 0:
        km = round(km)

    label3.config(text=f"{km}")


miles_entry = Entry(width=14, justify="center")
miles_entry.grid(column=1, row=0)

label = Label(text="Miles")
label.grid(column=3, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=3, row=1)

convert_button = Button(text="Calculate", command=button_pressed)
convert_button.grid(column=1, row=2)

radio_button1 = Radiobutton(text="Rounded       ", value=0, variable=round_state)
radio_button1.grid(column=4, row=0)

radio_button2 = Radiobutton(text="Not Rounded", value=1, variable=round_state)
radio_button2.grid(column=4, row=1)

window.mainloop()
