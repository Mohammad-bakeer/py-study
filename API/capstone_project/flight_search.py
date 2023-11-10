import os
import requests
from dotenv import load_dotenv, dotenv_values

load_dotenv()
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,):
        pass


        
    def search(self, city=""):
        url = os.getenv("URL2")
        parameters = {
            "term" : city,
            "location_types":"city"
        }
        headers = {
            "apikey":os.getenv("API_KEY")
        }
        response = requests.get(url=url, params=parameters, headers=headers)
        data = response.json()["locations"][0]["code"]
        print(response.text)
        print(data)
        return data
    
    