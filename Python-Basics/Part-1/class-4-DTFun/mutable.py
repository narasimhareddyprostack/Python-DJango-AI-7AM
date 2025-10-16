enames=["Rahul","Sonia","Priyanka"]
eids={101,102,103,103}
emp={
    'eid':101,
    'ename':"Rahul"
}
ba=bytearray([10,20,30,130])

print(type(enames))
print(type(eids))
print(type(emp))
print(type(ba))

enames[0] = "Rahul Gandhi"
print(enames)
eids.add(200)
print(eids)

emp['loc']="Wayanad"
print(emp)