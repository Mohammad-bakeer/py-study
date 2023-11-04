import smtplib

my_email= "test.1xm2@gmail.com"
password = "ylqglrmqjxspgenv"

connection = smtplib.SMTP("smtp.gmail.com"gitg)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="bakeermohammad11@gmail.com",msg="Helloo")
connection.close()