import requests

response=requests.get('https://dummyjson.com/products')

products=response.json()['products']
total=response.json()['total']
print(len(products))   #30
print(total)   #194