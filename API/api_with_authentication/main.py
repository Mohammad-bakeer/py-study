import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv, dotenv_values


API_KEY = "3682b529607eb1266bea8e634d30d205"
# cnt = 5 for today, +8 for each day you want more
CNT = 5
account_sid = "AC8ae3b4b5214fc8ad746e4489de9ef5cd"
auth_token = "7add1ed881b45282e0e691f2c5913fc8"
# weather condition IDs:
# https://openweathermap.org/weather-conditions

paramerters = {
    "lon": 35.945,
    "lat": 31.9552,
    "units": "metric",
    "APPID": API_KEY,
    # "cnt": CNT,
}


response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=paramerters)
response.raise_for_status()

# day 1 hours:{index 0:9:00, index 1:12:00, index 2:15:00, index 3:18:00, index 4:21:00} check on chrome with json extension, try the chart view
will_rain = False

for i in range(35, 38):
    day = response.json()["list"][i]
    id = day["weather"][0]["id"]
    # check the website if you want more info about weather ids
    if (id < 700):
        will_rain = True

if will_rain:
    print("x")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body=f"bring an umbrella, it might rain around {day['dt_txt'].split()[1]}",
            from_="+12028385541",
            to="+962796747696"

        )
    print(message.status)
