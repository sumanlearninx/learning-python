# string methods

name = "Hello Suman"
name = "Hi Suman"
print(name) 
# prints Hi Suman -its not because the value is changed in memory address
# its because the reference of variable name changes from one memory address to another memory address
# since python itself manages garabage value, the previous memory address will be deleted

name = "Hello Suman"

for char in name:
    print(char, end = "")

print("....")

print(name.replace("Suman", "World")) # Hello World - it returns the new value, doesn't replace original
print(name) # Hello Suman - doesn;t change the original value because strings are immutable

print(name.lower())
print(name.upper())
print(name.title())

name = "   Hello Suman     "
print(name.lstrip()) # removes blank space from left side
print(name.rstrip()) # removes blank space from right side
print(name.strip()) # removes blank space from both side

name = "Hello Suman"
print(name.lstrip('H')) # ello Suman
print(name.rstrip('n')) # Hello Suma

data = 'a, b, c, d'
print(data.split(',')) # returns list ['a','b',....]