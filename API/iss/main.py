import requests
from datetime import datetime
import smtplib
import time
import os
from dotenv import load_dotenv, dotenv_values


load_dotenv()

MY_EMAIL= os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORDE")
MY_LAT = float(os.getenv("LAT"))
MY_LONG = float(os.getenv("LON"))

def is_iss_seeable():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        return True
def is_night():

    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True 

receiving_email = os.getenv("EMAIL2")
while True:
    time.sleep(60)
    if is_night() and is_iss_seeable():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=receiving_email,msg=f"Subject:Look UP\n\nthe ISS is above you in the sky")
