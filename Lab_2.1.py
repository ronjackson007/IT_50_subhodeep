# List
a = (1, 2, 3, "abc", 6, 8, 7)
print(list(a))

# Tuples

a = (1, 2, 3, "abc")
print(tuple(a))

# Dictionaries
x = {"Book": "Intro To Python", "year":2020}
print(dict(x))
y = dict(name="Book", year=2020)
print(y)

# Set
thisset = {"Book", "year", 2, 2, 2, "Book"}
print(thisset)

# Boolean
print(10==10)
print(10>9)
print(10<9, 10==10, 10>9)

# Example

a = 10
b = 3

if a > b:
    print("a is greater")
else:
    print("a is less")

# Number
x = 34e4
y = 12E9
print(x)
print(y)

# TypeConversion
x = 1
y = 2.3
z = 5j

a = float(x)
b = int(y)
print(a)
print(b)

import random
print(random.randrange(1, 9))

