import json 
fp=open('emp.json','r')
employees=json.load(fp)
print(employees)

for emp in employees:
    if emp['gender'] == 'Female':
        print("Employee Id-",emp['eid'],"and Employee Name:",emp['name'])