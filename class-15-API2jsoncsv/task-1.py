import json,csv,requests

response=requests.get('https://jsonplaceholder.typicode.com/users')
users=response.json()
print(type(users))
print(users)