from tkinter import *


def calculate():
    miles = float(miles_input.get())
    kilometers = round(miles * 1.609)
    result_label.config(text=f"{kilometers}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=65, pady=35)

# Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Is equal Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Kilometer Result Label
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# Kilometer Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)


window.mainloop()
