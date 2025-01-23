# functions - block of code to perform specific tasks

def add():
    num1 = 10
    num2 = 20
    print(num1 + num2)

add() # 30
add() # 30
add() # 30

# parameter function

def diff(num1, num2):
    print(num1 - num2)

diff(2, 2) # 0
diff(20, 25) # -5

# value return - one function must have only one return 
# and should be placed at the end of the function

def mult(num1, num2):
    return num1 * num2

a = mult(2, 3) 
b = mult(3, 5) 

print(a) # 6
print(b) # 15

# return multiple values

def calculate(num1, num2):
    sum = num1 + num2
    sub = num1 - num2
    prod = num1 * num2

    return sum, sub, prod

a,b,c = calculate(2, 3)

print(a) # 5
print(b) # -1
print(c) # 6

# lambda functions - anonymous functions
# we assign it to the variable which stores the reference of the variable

res = lambda : 10 + 20
print(res())

sub = lambda x,y : x - y
print(sub(20, 10))