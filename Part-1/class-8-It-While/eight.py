#print even numbers for loop?
#2,4,6,8,10

for num in range(2,11):
    if num%2 != 0:
        continue   #skip current iteration and execute nex
    print(num)