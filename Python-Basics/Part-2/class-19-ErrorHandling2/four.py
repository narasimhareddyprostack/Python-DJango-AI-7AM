try:
    a=int(input("Enter First No:"))
    b=int(input("Enter Secon No:"))
    print(a/b)          
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)

print("GM")