#wap to read appl.txt file and print data
fp=None
try:
    fp=open('abc.txt','r')
    data=fp.read()
    print(data)
except FileNotFoundError as err:
    print(err)
    fp=open("appl.txt",'r')
    data=fp.read()
    print(data)

finally:
    print("finally block -execute always")
    fp.close()
print("Good Morning")