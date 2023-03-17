# Write a function to reverse an array using function

n = int(input("Enter The No. of element: "))

arr1 = []
for i in range(0, n):
    it = input()
    arr1.append(it)
print(arr1)
def swap(arr1):
    arr2 = []
    for i in range(len(arr1)-1, -1, -1):
        arr2.append(arr1[i])
    print(arr2)

swap(arr1)

# Enter The No. of element: 3
# 4
# 5
# 6
# ['4', '5', '6']
# ['6', '5', '4']