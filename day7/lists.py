# list - collections of items
# Lists are MUTABLE -- elements can be changed

# creating list 
# elements are enclosed within square brackets [] separated by commas
# list can have multiple type elements as well and the duplicate elements as well

numbers = [1,2,3,4,5,6,7]
print(numbers)

# Indexing
print(numbers[3]) # 4

# Negative Indexing
print(numbers[-3]) # 5

# changing value
numbers[0] = 9
print(numbers) # change the element in 0 index to 9
numbers[0] = 1

# Slicing in lists
print(numbers[1:4]) # [2,3,4] # from 1 position to 3
print(numbers[2:]) # [3,4,5,6,7] # from 2 position to last
print(numbers[::]) # [1, 2, 3, 4, 5, 6, 7] # from start to last
print(numbers[::2]) # [1,3,5,7]  # from start to last with the step of 2
print(numbers[::-1]) # [7,6,5,4,3,2,1] # from last to start
print(numbers[::-2]) # [7,5,3,1] # from last to start with the step of 2

# len() - length of list
print(len(numbers)) # 7

# loop in list

for num in numbers:
    if num % 2 == 0:
        print(num, end = ",") # 2, 4, 6
    else:
        continue
print(".......")


# 2D List - matrix

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix) # [1,2,3], [4,5,6], [7,8,9]
print(matrix[1]) # [4,5,6]
print(matrix[1][2]) # [6]
print(matrix[::-1]) # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

# looping through 2D List

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()
