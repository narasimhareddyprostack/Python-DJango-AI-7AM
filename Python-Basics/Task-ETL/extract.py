import requests

response_data=requests.get('https://jsonplaceholder.typicode.com/users')
status_code=response_data.status_code;
users=response_data.json()
print(type(users))
print(status_code)