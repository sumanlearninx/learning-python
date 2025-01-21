# WAP for profit and loss

sp = float(input("Enter the selling price : "))
cp = float(input("Entr the cost price : "))

if sp > cp:
    print("It is profit.")
    print(sp - cp)

else:
    print("It is loss.")
    print(cp - sp)

# WAP to check if the number input is odd or even

num = int(input("Enter the number : "))

if num % 2 == 0:
    print("It is even")

else:
    print("It is odd")

# WAP to find the largest number among three numbers

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))

if num1 > num2 and num1 > num3:
    print("num1 is greater : ", num1)

elif num2 > num1 and num2 > num3:
    print("num2 is greater : ", num2)

else:
    print("num3 is greater : ", num3)


# WAP to assign the grade based on the marks
# WAP to print Fizz if a number is divisible by 3, Buzz if divisible by 5, FizzBuzz if number is 
# divisble by both 5 and 3.. else print the number as it is 

num = int(input("Enter a number : "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

elif num % 3 == 0:
    print("Fizz")

elif num % 5 == 0:
    print("Buzz")

else:
    print(num)