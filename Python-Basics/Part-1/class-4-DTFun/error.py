""" class while:
    pass
#syntaError """

""" eid=101
print(ename) #NameError """

""" 
def login():
print("Login Success") #IndendatonEerror """
""" 
b=bytes([10,20])
b[0]=11    #TypeError
 """

""" a=int(input("enter number only:"))  #ValueError
 """
""" 
emp={
    'eid':101,
    'ename':"Rahul"
}
print(emp['eid'])  #101
print(emp['ename'])  #Rahul
print(emp['loc'])  #KeyErrorKeyError: 'loc' """

""" 
eids=[10,20,30]
eids.append(40)
print(eids)
eids.login()  #AttributeError

 """

eids=[10,20,30]
#index 0  1  2
print(eids[0])   #10
print(eids[1])   #20
print(eids[2])  #30
print(eids[9])  #IndexError