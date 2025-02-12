
a = {}
print(type(a)) # <class 'dict'> - not set
b = set()
print(b) # set()

# remove duplicate elements from list

list1 = {1, 4, 6, 2, 7, 2, 1}
print(list(set(list1))) # [1, 2, 4, 6, 7]
