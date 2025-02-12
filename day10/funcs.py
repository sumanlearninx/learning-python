def sum(num1, num2=0):
    print(num1 + num2)

sum(1,7) # 8
sum(1) # 1

# multiple arguments

def add(*args):
    print(args) # (tuple)
    result = 0
    for i in args:
        result += i
    print(result)

add(1,2,3) # 6
add(1) # 1


# keyword arguments - returns the dictionary

def func(*args, **kwargs):
    print(args) # (1, 2, 3)
    print(kwargs) # {'name': 'suman', 'num1': 1}

func(1,2,3, name="suman", num1=1)

