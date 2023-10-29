from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200,height=200)
logo_pic = PhotoImage(file="password_manager/logo.png")
canvas.create_image(100,100, image=logo_pic)
canvas.grid(row=0,column=1)

wLabel=Label(text="Website: ")
wLabel.grid(row=1,column=0)

wtext = 

IdLabel=Label(text="Email/Username: ")
IdLabel.grid(row=2,column=0)

pLabel=Label(text="Password: ")
pLabel.grid(row=3,column=0)

window.mainloop()