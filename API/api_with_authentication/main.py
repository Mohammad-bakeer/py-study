import requests

API_KEY = "3682b529607eb1266bea8e634d30d205"

paramerters = {
    "lon":35.945,
    "lat":31.9552,
    "units":"metric",
    "APPID":API_KEY,
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/weather",params=paramerters)
response.raise_for_status()
main_temp = response.json()["main"]
print (f"temp: {main_temp['temp']}, what it feels like: {main_temp['feels_like']}")