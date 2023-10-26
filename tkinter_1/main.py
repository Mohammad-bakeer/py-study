from tkinter import *

window = Tk()
window.title("My First gUI Code")
window.minsize(500, 500)

input = Entry(width=18)
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 15, "normal"))
miles_label.grid(column=2, row=0)

label_1 = Label(text="is equal to: ", font=("Arial", 15, "normal"))
label_1.grid(column=0, row=1)

label_2 = Label(text=0, font=("Arial", 15, "normal"))
label_2.grid(column=1, row=1)

label_3 = Label(text="Km", font=("Arial", 15, "normal"))
label_3.grid(column=2, row=1)


def convert():
    x = (float(input.get())*1.609)
    label_2.config(text=x)


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
