numbers=[18,31,8,11,7,55,232]

def verify(num):
    return num%2==0

filter_obj=filter(verify,numbers)

print(list(filter_obj))
#print(list(filter(lambda num:num%2 ==0,numbers)))