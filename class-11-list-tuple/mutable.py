enames=["Rahul","Sonia","Priyanka",10,20]  #list-mutable
users=("Rahul","Sonia","Priyanka",10,20)  #tuple-immutable
enames[0]  = "Rahul Gandhi"
print(enames)
users[0]  = "Rahul Gandhi"
#TypeError: 'tuple' object does not support item assignment
