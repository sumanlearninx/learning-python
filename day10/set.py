# set - unordered collection of unique elements
# elements enclosed in curly brackets {} separated by commas
# sets are mutable - elements can be changed

# defining sets

set1 = {1,2,3,4,5} 
set2 = {3,4,5,6,7,8} 

print(set1) # {1, 2, 3, 4, 5}
print(set2) # {3, 4, 5, 6, 7, 8}

# add elements to set

set1.add(7)
print(set1) # {1, 2, 3, 4, 5, 7}

# remove elements 

set1.remove(5)
print(set1) # {1, 2, 3, 4, 7}

# remove elements using discard()
# remove() raises a KeyError if element not found in set
# discard() doesn't raise error

set1.discard(5)
print(set1) # # {1, 2, 3, 4, 7}

# Set Operations 

# union
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection
print(set1 & set2) # {3, 4, 7}

# Difference
print(set1 - set2) # {1,2}

# symmetric difference - (A-B) U (B-A)
print(set1 ^ set2) # {1, 2, 5, 6, 8}


# frozenset - this makes the set immutable

fs = frozenset({1,2,5,3,7})
print(fs) # frozenset({1, 2, 3, 5, 7})




