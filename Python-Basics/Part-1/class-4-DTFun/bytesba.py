#bytes type is immutable
b=bytes([10,20,30,40])   # 0 to 255
#index   0   1  2   3

#bytearray is Mutable object
ba=bytearray([10,20,30,40])   # 0 to 255
print(type(b))
print(type(ba))

########
#b[0] = 11  #Item Assigment not possible
ba[1] = 21

for ele in ba:
    print(ele)