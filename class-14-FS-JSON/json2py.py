#json.loads()  --> json str to py object
import json
emp_json_str='''
[
    {"eid":101,"ename":"Rahul","esal":45000.45,"avail":null,"promotion":true},
    {"eid":102,"ename":"Sonia","esal":55000.45,"avail":null,"promotion":false},
    {"eid":103,"ename":"Priya","esal":65000.45,"avail":null,"promotion":true}
]
'''
employees=json.loads(emp_json_str)
print(type(employees))  #<class,list>
print(employees)
for emp in employees:
    print(emp['ename'])