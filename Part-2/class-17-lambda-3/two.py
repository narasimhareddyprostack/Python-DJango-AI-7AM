from functools import reduce
numbers=[1,2,3,4,5,6]  #wap sum of n numbers

def sum_elements(a,b):
    return a+b 

#sum=reduce(lambda a,b:a+b,numbers)
sum=reduce(sum_elements,numbers)
print(sum)