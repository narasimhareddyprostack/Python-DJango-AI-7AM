enames=["Rahul","Sonia","Priyanka"]
#index   0        1              2
#index   -3         -2          -1
""" for ename in enames:
    print(ename) """
#itearte list object using while loop
'''
initilization st: i=0
condition     st: i<len(enames)
incr/desr     st: i=i+1
'''
i=0
while i<len(enames):
    print(enames[i])
    i=i+1