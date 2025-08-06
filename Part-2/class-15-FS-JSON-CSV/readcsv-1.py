#read users.csv file and print user names
import csv 
fp=open('users.csv','r')
user_reader=csv.reader(fp)
print(type(user_reader))  #<class '_csv.reader'>
print(user_reader)        #<_csv.reader object at 0x000001E4EDBCE920>

users=list(user_reader)
#excluing csv header
print(users[1:])   #list slicing

for user in users[1:]:
    print(user[1])