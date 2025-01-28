# list methods

numbers = [1,2,3,4,5,6,7]

numbers.append(8) # add element to the last of the list
print(numbers) # [1,2,3,4,5,6,7,8]

numbers.pop() # removes the last element from list
print(numbers) # [1,2,3,4,5,6,7]

numbers.pop(1) # removes the element at index 1
print(numbers) # [1, 3, 4, 5, 6, 7]

numbers.insert(1, 2) # insert the element 2 at index 1
print(numbers) # [1, 2, 3, 4, 5, 6, 7]

"""
    Note : insert adds the element to the specific index
            append adds the element to the last index
            however, append is recommended to use than insert 
            because, using insert changes the index of other elements which is more complex

"""

numbers.remove(3) # removes 3 from the list. it take the element as parameter not the position
print(numbers) # [1, 2, 4, 5, 6, 7]


# add two lists - extend

list1 = [1,2,3]
list2 = [3,4,5,6]

new_list = list1 + list2
print(new_list) # [1, 2, 3, 3, 4, 5, 6]

list1.extend(list2)
print(list1) # [1, 2, 3, 3, 4, 5, 6]
