'''
Rest API URL: https://jsonplaceholder.typicode.com/users
Method Type : GET
Required Fields: None
Access Type: Public
'''
import requests
url='https://jsonplaceholder.typicode.com/users'
response=requests.get(url)
print(type(response))
users=response.json()
print(type(users))
