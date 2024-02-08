from datetime import datetime

import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "jarearms"
TOKEN = "dfhir3456jkhaJILoremIpsum2367"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# create the graph

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "Minutes",
#     "type": "int",
#     "color": "sora"
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# post a pixel to the graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

graph_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "95"
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240207"

update_params = {
    "quantity": "110"
}

# update a pixel based on a date

# response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)

# delete a pixel

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240207"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
