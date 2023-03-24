# Demonstrate a python code to print Try, Except, Else and Finally block statement
def div(x, y):
    try:
        res = x/y
    except ZeroDivisionError:
        print("Sorry! You are dividing by zero")
    else:
        print("Your answer is: ", res)
    finally:
        print("This is Always executed")
div(3, 0)
div(1, 2)
