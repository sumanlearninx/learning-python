# list comprehension

# to print the squares of numbers from 1 to 10

# normal method
sq = []
for i in range(1,11):
    sq.append(i ** 2)
print(sq) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# list comprehension method

# [expression for item in iterable if condition]

sq = [i ** 2 for i in range (1,11)]
print(sq) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# condition in list comprehension

sq = [i ** 2 for i in range(1,11) if i**2 % 2 == 0 ]
print(sq) # [4, 16, 36, 64, 100]

# using comprehension list, print None if the number is odd and print that number if it is even

none_list = [i if i%2 == 0 else None for i in range(1,9)]
print(none_list)
