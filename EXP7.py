# Write a python program to find reverse of an array using 4 different methods

arr = [1, 3, 4, 5, 6]
print(arr)

print("|||||||||||||||")

# met 1: Using slicing
rev = arr[::-1]
print(rev)

# met 2: By using reverse function
arr.reverse()
print(arr)
# met 3
arr1 = [10, 20, 30, 40]
res = list(reversed(arr1))
print(res)

# met 4: using iteration
arr2 = []
for i in range(4, 0):
    arr2.append(arr[i])
print(arr)
# Output
# [1, 3, 4, 5, 6]
# |||||||||||||||
# [6, 5, 4, 3, 1]
# [6, 5, 4, 3, 1]
# [40, 30, 20, 10]
# [6, 5, 4, 3, 1]