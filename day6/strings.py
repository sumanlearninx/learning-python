# strings - alphanumeric value
# strings are immutable 
# mutable - whose value can be changed
# immutable - whose value cannot be changed # strings, int, float

# single line string 
sls = "hello single line"

print(sls)

# multi line string

mls = """
hello multi line string
hi
bye
"""
print(mls)

# indexing - zero based string

fruit = "apple"
print(fruit[0]) # a
print(fruit[4]) # e

# negative indexing - count from the end of the string

s = "Suman"
print(s[4]) # n
print(s[-4]) # u

# s[0] = "a" - TypeError : Strings are immutable

# slicing

name = "suman"
print(name[0:4]) # suma
print(name[::]) # prints 0 to last - suman
print(name[::2]) # prints 0 to last with the step of 2 - smn

# len() - returns the length of the string

print(len(name)) # 5

# characters vs substrings

# characters - single item in string
# substring - portion of string 

