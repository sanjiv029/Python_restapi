import requests

endpoint = "http://127.0.0.1:8000/api/products/55/"

get_response = requests.get(endpoint) 
print("Response JSON:", get_response.json())  
