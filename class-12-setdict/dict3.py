emp={'eid':101,
    'ename':'Rahul',
    'esal':45000.45
}
#print all keys  - dict.keys() method
for key in emp.keys():
    print(key)
print("**********")
#print all values - dict.values() method
for value in emp.values():
    print(value)
print("**********")
#print all key:values -dict.items() method
for key,value in emp.items():
    print(key,value)
