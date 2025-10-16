fp=open('data.txt','r')
#to know about fp file pointer info.
print(fp.name)    #data.txt
print(fp.mode)    # r 
print(fp.readable()) #True
print(fp.writable()) #False
print(fp.closed)     #False
fp.close()
print(fp.closed)     #True