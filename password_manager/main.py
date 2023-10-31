from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    p_entry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = w_entry.get()
    username = id_entry.get()
    password = p_entry.get()

    if len(website) == 0 or len(password)==0:
        messagebox.showerror(title="oops", message="Please fill all the fields") 
    else:
        with open("password_manager/data.txt", "a") as data_file:
            data_file.write(f"{website} - {username} - {password}\n")
            w_entry.delete(0,END)
            p_entry.delete(0,END)
            messagebox.showinfo(title="DONE", message="info saved")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
logo_pic = PhotoImage(file="password_manager/logo.png")
canvas.create_image(100,100, image=logo_pic)
canvas.grid(row=0,column=1)

#labels
wLabel=Label(text="Website: ")
wLabel.grid(row=1,column=0)

IdLabel=Label(text="Email/Username: ")
IdLabel.grid(row=2,column=0)

pLabel=Label(text="Password: ")
pLabel.grid(row=3,column=0)


#entries --------------------------------------------#
w_entry = Entry(width=35)                            #
w_entry.grid(row=1,column=1,columnspan=2)            #
w_entry.focus()                                      #
                                                     #
id_entry = Entry(width=35)                           #
id_entry.grid(row=2, column=1, columnspan=2)         #
id_entry.insert(0,"yourdefaultemail@gmail.com")      #
                                                     #
p_entry = Entry(width=25)                            #
p_entry.grid(row=3, column=1,columnspan=1)           #
#----------------------------------------------------#

p_button = Button(text="Generate Password", command=generate_password)
p_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()