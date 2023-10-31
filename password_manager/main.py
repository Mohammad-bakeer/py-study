from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
logo_pic = PhotoImage(file="password_manager/logo.png")
canvas.create_image(100,100, image=logo_pic)
canvas.grid(row=0,column=1)


wLabel=Label(text="Website: ")
wLabel.grid(row=1,column=0)
IdLabel=Label(text="Email/Username: ")
IdLabel.grid(row=2,column=0)
pLabel=Label(text="Password: ")
pLabel.grid(row=3,column=0)


w_entry = Entry(width=35)
w_entry.grid(row=1,column=1,columnspan=2)
id_entry = Entry(width=35)
id_entry.grid(row=2, column=1, columnspan=2)
p_entry = Entry(width=21)
p_entry.grid(row=3, column=1,columnspan=1)


p_button = Button(text="Generate Password")
p_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()