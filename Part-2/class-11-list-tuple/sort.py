enames=["Rahul","Sonia","Priya"]
unames=("Rahul","Sonia","Priya")
enames.sort()
print(enames)
#unames.sort()

#how to sort list object  - list.sort() method
#how to sort tuple object - no sort method because tuple is immutable
'''
sorted() - inbuilt function, to sort seqeunces
'''
result=tuple(sorted(unames))
print(result)