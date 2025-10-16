a=None
b=None

try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    print(a/b)
except ZeroDivisionError as err:
    print(err)   #10.0

print("GM")