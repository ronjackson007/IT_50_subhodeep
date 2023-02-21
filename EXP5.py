# Write a python frogram to find the factorial of the given number
num = int(input("Enter a number: "))

def factorial(num):
    if num == 0:
        return 1
    else:
        fact = num*factorial(num-1)
        print(num, fact)
        return fact

print("Factorial is ",factorial(num))

# Enter a number: 5
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120
# Factorial is  120

# Enter a number: 0
# Factorial is  1