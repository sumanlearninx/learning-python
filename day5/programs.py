# enter two numbers : eg 3 and 5
# create the multiplication table from 3 to 5
# standard format of table 
# use function which takes two numbers as parameters
def mult_table(num1, num2):
    for i in range(num1, num2):
        print(f"Multiplication table of {i} is :")
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")
        print("........")
    
mult_table(3,8)


# function that returns the sum of first n numbers

def sum_n(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    
    return sum

res = sum_n(100)
print(res)


# function that prints even numbers 1 to 100

def print_even():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)
        else:
            continue


print_even()

# function that returns True if the number is palindrome else false

def is_palindrome(num):
    original_num = num
    rev = 0

    while num!=0:
        rem = num % 10
        num = num // 10
        rev = (rev * 10) + rem
    
    if original_num == rev:
        return True
    else:
        return False

res1 = is_palindrome(1001)
print(res1) # true

res2 = is_palindrome(1234)
print(res2) # false


# function that returns whether a number is prime or not

def is_prime(num):
    val = 0
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            val += 1

    if val > 0:
        return "Not prime"
    
    else:
        return "Prime"
num = int(input("Enter the number : "))
res = is_prime(num)
print(res)
