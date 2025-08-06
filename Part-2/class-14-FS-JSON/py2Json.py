import json 

employees=[
    {'eid': 101, 'ename': 'Rahul', 'esal': 45000.45, 'avail': None, 'promotion': True}, 
    {'eid': 102, 'ename': 'Sonia', 'esal': 55000.45, 'avail': None, 'promotion': False}, 
    {'eid': 103, 'ename': 'Priya', 'esal': 65000.45, 'avail': None, 'promotion': True}
]
#convert to python object to json str
emp_json_st=json.dumps(employees)
print(emp_json_st)