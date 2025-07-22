enames=["RG","SG","PG"]
eids=(101,102,103,104)
uids={101,101,101,101}  #duplicates are not allowed
ename="Rahul"

print("RG" in enames)   #True
print(109 in eids)      #False
print(102 in uids)      #False
print('z' in ename)     #False