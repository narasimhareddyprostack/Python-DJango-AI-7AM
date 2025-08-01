fp=open('data.txt','r')
#data=fp.read()
#data=fp.readline(26)
data=fp.readlines()
print(data[0:2])

fp.close()

