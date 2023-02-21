# Write a python frogram to find the factorial of the given number
num = int(input("Enter a number: "))

def factorial(num):
    if num == 0:
        return 1
    else:
        fact = num*factorial(num-1)
        print(num, fact)
        return fact

print(factorial(num))

# Enter a number: 10
# 3628800
# Enter a number: 0
# 1