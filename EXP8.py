#Write a python function that takes two lists and returns addition of two lists elements
n = int(input("Enter The No. of element: "))

arr1 = []
for i in range(0, n):
    it = input()
    arr1.append(it)
print(arr1)
arr2 = []
for i in range(0, n):
    it = input()
    arr2.append(it)
print(arr2)

def addition(arr1, arr2):
    arr3 = []
    for i in range(0, n):
        res = int(arr1[i]) + int(arr2[i])
        arr3.append(res)
    print(arr3)

addition(arr1, arr2)

# Enter The No. of element: 2
# 1
# 2
# ['1', '2']
# 4
# 3
# ['4', '3']
# [5, 5]
