# mutable-list can change or modify
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[3] = 99
print(a)

# immutable-tuples can't change or modify

t = (1, 2, 3, 4, 5, 6, 7, 8)
print(t)
# t[0] = 99  'tuple' object does not support item assignment
t = (1,)
print(t)

# Exchange values

a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# Input Functions

num = int(input("Enter Your Number : "))
print(num)

string = str(input("Enter a String: "))
print(string)

Name = input("Enter a Name: ")
print("Name is " + Name)

# Condition

var1 = 0
var2 = 1
var3 = 2
if var1 > var2:
    print("var1 is greater")
else:
    print("var2 is greater")

var4 = int(input())
if var4 > var2:
    print("var4 is greater")
elif var4 == var2:
    print("var4 is equal")
else:
    print("var4 is smaller")



