""" def add(a,b):
    return a+b 

 """
#how to invoke add function?  - using functon name ie add()
#how to invoke lambda express/function?

#assign your lambda express to variable
eid=101
add=lambda a,b:a+b 

print(type(eid))   #<class,int>
print(type(add))   #<class,function>
#how to execute/invoke function? using function name
r1=add(10,20)

print(r1)
