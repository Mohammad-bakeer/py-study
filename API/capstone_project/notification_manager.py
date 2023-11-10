import smtplib
import os
from dotenv import load_dotenv, dotenv_values


load_dotenv()

my_email= os.getenv("EMAIL")
password = os.getenv("PASSWORD")
to_email = os.getenv("S_EMAIL")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=to_email, msg=message)

    