eid=101
esal=45000.45
ename="Rahul Gandhi"
c=10+20j
avail=True            #flat value True - 1 and False -0 

eids=[101,102,103,104]

enames=("Rahul","Sonia","Priyanka","NM")

uids={101,102,101,102,101,101,102}

emp={
    'eid':101,
    'ename':"Rahul"
}



b=bytes([10,20,30,40])
ba=bytearray([10,20,30,40])
fz=frozenset({10,20,30})
r=range(10)
n = None


print(type(eid))    #<class,int>
print(type(esal))   #<class,float>
print(type(ename))   #<class,string>
print(type(c))   #<class,complex>
print(type(avail))   #<class,bool>


#how to find data type
print(type(eids))
print(type(enames))
print(type(uids))
print(type(emp))


#how to find the Data type
print(type(b))
print(type(ba))
print(type(fz))
print(type(r))
print(type(n))