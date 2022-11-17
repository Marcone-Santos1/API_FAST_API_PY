import requests
import json

# json body
# {
#     "id": 4,
#     "name": "Phone Sony",
#     "price": 1000,
#     "brand": "Samsung",
#     "quantity": 10
# }

class Product:
    
    def __init__(self) -> None:
        self.url = "http://127.0.0.1:8000/products/"
    
    def create_product(self, product: dict):

        payload = json.dumps(product)
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", self.url, headers=headers, data=payload)

        print(response.text)
        
    def get_all_product(self):

        payload = ""
        headers = {}

        response = requests.request("GET", self.url, headers=headers, data=payload)

        print(response.text)
        
    def get_one_product(self, product_id):

        url = f"{self.url}{str(product_id)}"
        print(url)

        payload = ""
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
        
    def update_product(self, _id, _name, _price, _brand, _quantity):
        
        url = f"{self.url}{str(_id)}"

        payload = json.dumps({
        "id": _id,
        "name": _name,
        "price": _price,
        "brand": _brand,
        "quantity": _quantity
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text)
    
    def delete_product(self, product_id):

        url = f"{self.url}{str(product_id)}"

        payload = ""
        headers = {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text)