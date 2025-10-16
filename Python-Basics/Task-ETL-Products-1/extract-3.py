import requests

#response=requests.get('https://dummyjson.com/products')
products=requests.get('https://dummyjson.com/products').json()['products']
print(len(products))
