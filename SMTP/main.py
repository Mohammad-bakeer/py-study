import smtplib
from datetime import datetime 
import random
import pandas

my_email= "test.1xm2@gmail.com"
password = "ylqglrmqjxspgenv"

now = datetime.now()
today = (now.month,now.day)

data = pandas.read_csv("SMTP/birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    print(birthday_person["email"])
    file_path = f"SMTP/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file=file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday\n\n{contents}")
        