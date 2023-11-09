import os
import requests
from dotenv import load_dotenv, dotenv_values
from datetime import datetime

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
GENDER = os.getenv("GENDER")
AGE = os.getenv("AGE")
HEIGHT = os.getenv("HEIGHT")
WEIGHT = os.getenv("WEIGHT")


url = "https://trackapi.nutritionix.com/v2/natural/exercise"
url2 = os.getenv("URL2")

query_text = input("tell me which exercises you did: ")


parameters = {

    "query": query_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE

}

headers = {
    "x-app-id" :APP_ID,
    "x-app-key": API_KEY,  
}

response = requests.post(url=url, json=parameters, headers=headers)
result = response.json()

#date in dd/mm/yyyy format
today_date = datetime.now().strftime("%d/%m/%Y")
#time in 00:00:00 format 24H
now_time = datetime.now().strftime("%X")

#each exercise is a list item
for exercise in result["exercises"]:

    sheet_inputs = {
        #the name should look like your sheet name
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }

token = os.getenv("TOKEN")
headers_2 = {
   "Authorization" : f"Bearer {token}"
}

response2 = requests.post(url=url2,json=sheet_inputs,headers=headers_2)
response2.raise_for_status()