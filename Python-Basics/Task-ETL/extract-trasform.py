import requests

response_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=response_data.json()

#traform-for Mysql Table
new_users=[]
for user in users:
    new_users.append((user['id'],
                      user['username'],
                      user['email'],
                      user['address']['city'],
                      user['phone']))

print(new_users)
