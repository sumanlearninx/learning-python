# control structure - loop
# for loop - used when we know the number of iterations
# while loop - when we don't know the number of iterations

for i in range(10):
    print("python", i)

# factorial

num = 5
fact = 1

for i in range(1, num+1):
    fact = fact * i

print(fact) 


# while loop
num = 10
fact = 1
while num > 0:
    fact = fact * num
    num = num - 1

print(fact)

# break - continue

for i in range(10):
    if i == 3:
        break

    print(i) # 0, 1, 2

for i in range(10):
    if i == 3:
        continue

    print(i, end = " ") # prints 0 to 9 except 3

# pass - it is like a placeholder which tells there will be code added later

for i in range(5):
    pass
    print(i)