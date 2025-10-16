emp={'eid':101,'ename':'Rahul','ename':'Rahul Gandhi'}
print(emp)
print(type(emp))

#how to read dict values - using key
print(emp['eid'])    #101
print(emp['ename'])  #Rahul Gandhi
#print(emp['loc'])    #KeyError: 'loc'

print(emp.get('loc'))  #None