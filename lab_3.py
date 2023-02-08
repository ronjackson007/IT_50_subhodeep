# List Operations
#To access List Items
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print(list(a))
print(a[6])

# List Slice Operations

print(a[2:6])
print(a[2:])
print(a[:3])

# Extended slicing operations
print(a[2:10:2])

# to sort and reverse the list

a.sort()
print(a)
a.reverse()
print(a)

# append
a.append(44)
a.append(44)
a.append(44)
print(a)

b = []
b.append(1)
b.append(66)
b.append(6)
b.append(5)
b.append(3)
print(b)

# insert
print("insert")
b.insert(0,9)
b.insert(1,99)
print(b)
# remove
b.remove(66)
print(b)

# pop
b.pop()
print(b)
b.pop(1)
print(b)



