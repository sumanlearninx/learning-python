# oop - object oriented programming
# class - blueprint for creating objects (instances) 
# that have attributes (variables) and methods (functions)

# creating a class

# class attributes are common among all objects 
# they are accessed through class

# __init__ 
# class constructor
# automatically invoked when the object is created

# self
# represents the current object

class User:
   
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def greet(self):
        print(f"Hello, {self.username}")

user1 = User("suman", "1234")
user2 = User("sanam", "pass")

# accessing objects attributes
print(user1.username) # suman
print(user2.password) # pass

# accessing methods
user1.greet() # Hello, suman