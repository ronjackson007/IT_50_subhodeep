#Create a tuple and perform the following operations:
#1. Add Items
#2. length
#3. Check for item in tuple
#4. Access items

t = ("Apple", "banana", "cherry", "orange")
t2 = ('mango',)
print(t)

# 1. Add Items

# t[4] = 'mango'
# TypeError: 'tuple' object does not support item assignment
t1 = t + t2
print(t1)

# 2. length
print(len(t))

# 3. Check for item in tuple
a = 'Apple'
if a in t:
    print("It is present in tuple")
else:
    print("It is not present in tuple")

# 4. Access items
print(t[0])
print(t[1])
for i in range(0, 3):
    print(t[i])

# Output
# ('Apple', 'banana', 'cherry', 'orange')
# ('Apple', 'banana', 'cherry', 'orange', 'mango')
# 4
# It is present in tuple
# Apple
# banana
# Apple
# banana
# cherry