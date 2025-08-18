import requests

response=requests.get('https://dummyjson.com/products')

print(type(response))
print(response.status_code)
print(response.json())


product_data=response.json()
#print(product_data)
print(type(product_data))