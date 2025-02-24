
import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "This field is done World"
}

get_response = requests.post(endpoint, json=data) 
print("Response JSON:", get_response.json())  
