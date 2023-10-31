    with open("password_manager/data.txt", "a") as data_file:
            data_file.write(f"{website} - {username} - {password}\n")
            w_entry.delete(0,END)
            p_entry.delete(0,END)
