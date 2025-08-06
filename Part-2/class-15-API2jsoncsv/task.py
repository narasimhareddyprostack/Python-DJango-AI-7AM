import json,csv,requests

response=requests.get('https://jsonplaceholder.typicode.com/users')
users=response.json()
#tranform users data for csv file
employees=[]
for user in users:
    employees.append((user['id'],user['username'],user['phone'],user['address']['city']))

#print(employees)


#write/load user data into new json file user.json
fp1=open('user.json','w')
json.dump(users,fp1)
print("New user.json file created")
#write user data into new csv file - user.csv
fp2=open('user.csv','w',newline="")
cw=csv.writer(fp2)
#write csv file - header
cw.writerow(['eid','ename','phoneno','city'])
cw.writerows(employees)
print("New File user.csv file created")

fp1.close()
fp2.close()