enames=["RG","SG","PG","RG","SG","SG","NM"]
#index   0    1     2    3     4   5   6 

#list methods
#l.count(ele) method return no of occurances specified element
print(enames.count("SG"))  #  3
#l.index(ele) method - return index of first occurance of specified elment
print(enames.index('SG'))  #
#l.append(ele) = add element end of list
enames.append("Amith")
print(enames)

enames.sort()  #Natural Sorting ie ASEC (A-Z and 0-9)
print(enames)
enames.sort(reverse=True)
print(enames)