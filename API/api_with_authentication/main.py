import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv, dotenv_values

load_dotenv()
API_KEY = os.getenv("API_KEY_")
# cnt = 5 for today, +8 for each day you want more
CNT = 5
account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOK")
# weather condition IDs:
# https://openweathermap.org/weather-conditions

paramerters = {
    "lon": os.getenv("LON"),
    "lat": os.getenv("LAT"),
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
    receiving_phone = os.getenv("PH_NUM_T")
    sending_phone = os.getenv("PH_NUM_S")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body=f"bring an umbrella, it might rain around {day['dt_txt'].split()[1]}",
            from_=sending_phone,
            to=receiving_phone

        )
    print(message.status)
