enames=["rahul",'sonia','priya']
#collect all employee name as uppercase in new list?

def change_case(ename):
    return ename.upper()

new_enames=list(map(change_case,enames))

print(enames)
print(new_enames)