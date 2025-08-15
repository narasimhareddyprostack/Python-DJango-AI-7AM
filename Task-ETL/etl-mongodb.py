import requests,mysql.connector,pymongo

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


#load data into mongodb collection
try:
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['dbone']
    users_col=db['users']
    users_col.insert_many(new_users)
    print("Data Inserted successfully mongodb")

except:
    print("Error while connection to mongoDB")

finally:
    pass