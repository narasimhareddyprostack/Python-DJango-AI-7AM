#read users.csv file and print user names
import csv 
fp=open('users.csv','r')
user_reader=csv.reader(fp)
users=list(user_reader)

for user in users[1:]:
    print(user[1])