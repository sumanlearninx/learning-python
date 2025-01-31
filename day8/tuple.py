# tuple 
# immutable - cannot be modified once they are created
# elements are separated by small braacket


# creating a tuple
t = (1,2,3,4,5,1)
print(t) # (1,2,3,4,5,1)

# Accessing elements by index / Negative Indexing
print(t[1]) # 2
print(t[-2]) # 5

# Tuple Methods
print(t.count(1)) # 2 - counts the number of occurence of times of elements
print(t.index(1)) # 0 - returns the first index of the element

# Tuple slicing
print(t[::2]) # (1,3,5)
print(t[::-1]) # (1, 5, 4, 3, 2, 1)

# loop in tuple
for element in t:
    if element>3:
        print(element) # 4, 5

# Type casting
print(type(t)) # <class 'tuple'>

# tuple to list
l = list(t)
print("List:",l) # List: [1, 2, 3, 4, 5, 1]

# list to tuple
t = tuple(l)
print(t) # (1, 2, 3, 4, 5, 1)

# Unpacking of tuples
numbers = (1,2,3,4)
a, b, c,d = numbers
print(a) # 1
print(d) # 4

# a, b, c, d, e = numbers ---- print(e) # Value Error : 