import os
import requests
from dotenv import load_dotenv, dotenv_values
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
load_dotenv()

ORIGIN_CITY_IATA = "LON"
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
   
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight == None:
        continue
    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city} -{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
                
        if flight.stop_overs > 0:
            message += f"\nFlight has 1 stop over, via {flight.via_city}."
            
        notification_manager.send_message(message=message, emails=emails)

