import smtplib
import datetime as dt
import random

my_email= "test.1xm2@gmail.com"
password = "ylqglrmqjxspgenv"

now = dt.datetime.now()
print(now.day)
weekday = now.weekday()

if(weekday==5): 
    with open(file="SMTP/quotes.txt") as qf:
        all_quotes = qf.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="bakeermohammad11@gmail.com",msg=f"Subject:{now.day}-{now.month}-{now.year} Quote\n\n{quote}")
        