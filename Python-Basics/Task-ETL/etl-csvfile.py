import requests,mysql.connector,pymongo,json,csv

#extract from source-Rest API/Cloud/Data WH/Files/Databases
response_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=response_data.json()

#tranform data - csv file
new_users=[]

for user in users:
    new_users.append((user['id'],user['username'],user['email']))

#print(new_users)

#load data into -new CSV file

fp=None 
try:
    fp=open("users.csv",'w',newline='')
    cw=csv.writer(fp)
    cw.writerow(['userId','userName','email'])
    cw.writerows(new_users)
    print("New CSV File created!")
    
except:
    print("Unable created new CSV File") 
finally:
    fp.close()

