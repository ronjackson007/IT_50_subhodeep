# WAP to use split and join methods in the string
# Join
# m-1
print("JOIN")
list = ['a', 'b', 'c']
a = " and ".join(list)
print(a)

# m-2
for i in list:
    print(i, "and", end=" ")
print("\nSPLIT")
# Split
str = "SDFf fwwf Wfwwf"
b = str.split()
print(b)
c = str.split(" ", 1)
print(c)
# OUTPUT
# JOIN
# a and b and c
# a and b and c and
# SPLIT
# ['SDFf', 'fwwf', 'Wfwwf']
# ['SDFf', 'fwwf Wfwwf']