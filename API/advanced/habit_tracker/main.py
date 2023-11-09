import os
import requests
from dotenv import load_dotenv, dotenv_values
from datetime import datetime

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
user_name = os.getenv("USER_NAME")
token = os.getenv("TOKEN")

user_parameters = {
    "token": token,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#already did it
#requests.post(url=pixela_endpoint, json=user_parameters)

graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"

id_ = os.getenv("ID")
name = os.getenv("NAME")

headers = {
    "X-USER-TOKEN": token
}

graph_config = {
    "id": id_,
    "name": name,
    "unit": "pages",
    "type": "int",
    "color":"momiji",
    "timezone": "Asia/Amman",
}

#requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{graph_endpoint}/{id_}"

optional_data = {
    "book_type": "WN",
    "book_name": "Kafka on the shore"
}

date = datetime.today().strftime("%Y%m%d")

pixel_config = {
    "date" : date,
    "quantity":"15",
    "optional_data":optional_data,
}

#requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
