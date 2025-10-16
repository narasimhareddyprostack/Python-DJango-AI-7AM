#read json file, and employee names
import json 
fp=open("emp.json",'r')
employees=json.load(fp)
print(employees)

for emp in employees:
    print(emp['ename'])