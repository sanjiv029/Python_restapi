# import requests

# # endpoint = "https://httpbin.org/status/200"  #your url here
# # endpoint = "https://httpbin.org/anything" 
# endpoint  = "http://127.0.0.1:8000/api/"
# get_response = requests.get(endpoint, json={"query":"Hello World"}) #API call Emulate http request
# print(get_response.text)
# print(get_response.json())
# print(get_response.status_code)

# #HTTP REQUEST ->Html
# #Rest api http request -> JSON

import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title": "Hello World"})  # API call

# print("Response Text:", get_response.text) 
print("Response JSON:", get_response.json())  
