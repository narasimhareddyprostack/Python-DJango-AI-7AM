#read command line arguments and print sum of values?
from sys import argv
print(argv)

numbers=argv[1:]   #list slice
print(numbers)

#iterate list ie numbers print sum of list valus

sum=0
for num in numbers:
    sum=sum+int(num) 

print(sum)