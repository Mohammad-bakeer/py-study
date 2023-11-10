import os
import requests
from dotenv import load_dotenv, dotenv_values

URL = os.getenv("URL_D")
load_dotenv()


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        response = requests.get(url=URL)
        self.departure_city
        self.departure_airport_code
        self. price
