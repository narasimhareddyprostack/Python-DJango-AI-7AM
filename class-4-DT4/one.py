l=[]  #empty list object
eids=[101,102,103]
uids=[101,101,101,102]  #duplicate are alloed
elements=[10,20.5,{},(),"Rahul"] #allowed heterogenous elemnets

#read
print(l)
print(eids)
print(uids)
print(elements)

#delete

del elements

print(elements)   #NameError