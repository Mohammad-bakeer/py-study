import os
import requests
from dotenv import load_dotenv, dotenv_values
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

load_dotenv()
data_manager = DataManager

sheet_data = data_manager.get_destination_data()

count = 2
"""
this was used to populate the iata fields  
for des in sheet_data:
    x = FlightSearch()
    code = x.search(des["city"])
    parameter = {
    "price":{
        "iataCode":code
    }
}
    url = f"{os.getenv('URL')}/{des}"
    res = requests.put(url=url,json=parameter) 
    count+=1
    """