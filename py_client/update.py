import requests

product_id = input("What is the product_id of the product you want to update? ")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not valid') 

if product_id:    
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/update/"
    data = {
    "title": "This field is done"
    }   
    get_response = requests.put(endpoint, json=data) 
    print("Response JSON:", get_response.json())  


