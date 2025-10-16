import requests,mysql.connector,pymongo,json

#extract from source-Rest API/Cloud/Data WH/Files/Databases
response_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=response_data.json()

#tranform data - mongodb 
new_users=[]

for user in users:
    new_users.append({'uid':user['id'],
                      'uname':user['username'],
                      'city':user['address']['city']})
#print(new_users)


#load data into new json file - users.json
fp=None 
try:
    fp=open('users.json','w')
    json.dump(new_users,fp)
    print("New Json file ie - users.json created!")
except:
    pass
finally:
    fp.close()
