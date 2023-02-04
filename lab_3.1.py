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
print("NAme is " + Name)


