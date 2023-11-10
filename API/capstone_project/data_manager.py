import os
import requests
from dotenv import load_dotenv, dotenv_values

URL_1 = os.getenv("URL_DM")
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=URL_1)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    