# WAP to count the no of characters and store them in a dictionary data structure
# METHOD 1
dict = {}
str = input("Enter a string: ")

for i in str:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
print(dict)

# METHOD 2
