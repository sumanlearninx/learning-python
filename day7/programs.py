# add all the elements of 2D list

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

sum = 0

for row in matrix:
    for num in row:
        sum += num

print(sum)

# min max numbers from list

nums = [6, 5, 6,8, 7, 2, 6, 5]
min = nums[0]
max = nums[0]
for num in nums:
    if num > max:
        max = num
    if num < min:
        min = num
print(f"Max is {max} min is {min}")


# remove duplicate numbers from list

# method 1

dup = []
for num in nums:
    if num in dup:
        dup.remove(num)
    dup.append(num)
print(dup)

# method 2

for num in nums:
    if num not in dup:
        dup.append(num)

print(dup)


# target sum = 5

nums = [1,2,4,3,3, 4,5,6]

target = []

for i in range(len(nums)):  
    for j in range(nums[i], len(nums)):
        if nums[i] + nums[j] == 5 and (nums[i],nums[j]) not in target:
            target.append((nums[i], nums[j]))
            
print(target)


list1 = [1, 3, 5, 6, 1]
list2 = [2, 3, 5, 7]

newlist = list1 + list2

union_list = []
inter_list = []

# for i in newlist:
#     if i not in union_list:
#         union_list.append(i)
        
# print(f"Union list : {union_list}")

# for i in list1:
#     for j in list2:

#         if i == j:
#             inter_list.append(i)

# print(f"Intersection : {inter_list}")



# Combining both above logic into one

for i in list1:
    for j in list2:

        if i not in union_list:
            union_list.append(i)
        
        if j not in union_list:
            union_list.append(j)

        if i == j:
            inter_list.append(i)

print(f"Intersection : {inter_list}")
print(f"Union list : {union_list}")


    
 