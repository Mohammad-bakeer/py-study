import os
import requests
from dotenv import load_dotenv, dotenv_values
load_dotenv()

URL_1 = os.getenv("URL_DM")
URL_2 = os.getenv("URL_DMU")
BEARER = os.environ['Authorization']
headers = {
        "Authorization": BEARER,
        "Content-Type": "application/json",
    }



class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=URL_1, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            updated_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{URL_1}/{city['id']}", json=updated_data, headers=headers)
    
    def get_customer_emails(self):
        response = requests.get(url=URL_2, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
            
