import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME= "sben834520"
TOKEN="sben834520"
GRAPH_ID = "graph2"
user_params = {
    "token": USERNAME,
    "username":TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",

}

#response = requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)

graph_enpoint= f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID ,
    "name": "Cycling Graph",
    "unit": "Ka",
    "type": "float",
    "color": "ajisai"
}
headers ={
    "X-USER-TOKEN": TOKEN
}
#respence = requests.post(url=graph_enpoint, json=graph_config, headers=headers)
#print(respence.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": "20230323",
    "quantity": "9.74"

}
#respence = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#print(respence.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime(year=2023, month=3, day=23).strftime('%Y%m%d')}"

new_pixel_data = {
    'quantity': '4.5'
}

respence = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(respence.text)

respence = requests.delete(url=update_endpoint, headers=headers)
print(respence.text)