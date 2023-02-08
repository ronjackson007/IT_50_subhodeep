# Short End if
a = 20
b = 34
if b > a: print("b is greater")
# Short Hand If ..... Else .....
a = 2
b = 34
print("a") if a > b else print("b is greater")

# One Line if else statements
a = 330
b = 330
print("a") if a > b else print("=") if a == b else print("b")

# And
# the and keyword is a logical operator, and is used to

a = 30
b = 3
c = 30

if a>b and c > b:
    print("a and c are greater than b")
else:
    print("c is greater")

# or
a = 30
b = 3
c = 0

if a>b or c > b:
    print("a or c are greater than b")
else:
    print("c is greater")

# Not
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# Nested If

a = 40

if a >10:
    print("Above 10")
    if a > 20:
        print("above 20")
    else:
        print("below 20")
else:
    print("Below 10")

# Pass Statement

a = 33
b = 50
if a > b:
    pass
