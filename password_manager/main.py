from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
p_entry = Entry(width=21)                            #
p_entry.grid(row=3, column=1,columnspan=1)           #
#----------------------------------------------------#

p_button = Button(text="Generate Password")
p_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()