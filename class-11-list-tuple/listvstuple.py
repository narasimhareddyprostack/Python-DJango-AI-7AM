enames=["Rahul","Sonia","Priya"]
users =("Rahul","Sonia","Priya")
#index   0         1        2
enames.append("NM")
#users.append("NM")   #AttributeError
print(enames.index("Sonia"))    #1
print(users.index("Sonia"))     #1
enames[0] ="Rahul Gandhi" 

print(enames)  
users[0] ="Rahul Gandhi"
print(users)