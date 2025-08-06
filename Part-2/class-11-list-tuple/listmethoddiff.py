#list.append(element) vs list.extend(seq/collectin of elemnt)
#list.clear() and del list

numbers=[10,20,30]
numbers.append(40)
print(numbers)
numbers.extend({50,60,70})
print(numbers)

#numbers.clear()
del numbers
print(numbers)
print(type(numbers))
