# 4 principle of OOP


# 1. encapsulation - data hiding - to private the attributes, use of __

# getter method - get_username -> to access the private attributes
# setter method - set_username -> to change the private attributes

# 2. abstraction
# hide the process

# 3. inheritance
# accessing the attributes and methods from parent class (base class) by child class
# and child class can have its own attributes and methods


# Types of inheritance
# 1. Single Inheritance

class Account():
    def __init__(self, accnum, balance):
        self.accnum = accnum
        self.balance = balance
    
    def get_acc_details(self):
        print(f"Account number : {self.accnum} Balance : {self.balance}")

class FDAccount(Account):
    def __init__(self, accnum, balance, interest):
        super().__init__(accnum,balance)
        self.interest = interest

fd = FDAccount('12345', 10000, 10)

fd.get_acc_details() # Account number : 12345 Balance : 10000


# 2 - multiple inheritance

# 3 - multilevel



# polymorphism - multiple forms
# method overriding - run time
# method overloading - compile time

class ParentClass:
    pass

class ChildClass(ParentClass):
    pass


# abstract class - objects of abstract class cannot be made
# abstract method - child class must override 

# access identifiers  - public, private, protected - attributes can be accessed only by base class


# MRO - multiple inheritance - method resolution order - left to right

# operator overloading


class Vector:
    def __init__(self, x, y) -> None:
        pass
    # def __str__(self) # it is used to override the memory adrress of x and y
# v1 = Vector(1,2)
# print(v1) - it prints memory address - so, def __str__