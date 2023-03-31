
# To open a file
# f = open("Hellotxt")
# content = f.read()
# print(content)
# f.close()

# f = open("Hellotxt", "r")
# content = f.read(3)
# print(content)
# content = f.read(3)
# print(content)
# f.close()

# readline
f = open("Hellotxt", "rt")
# print(f.readlines())
# print(f.readline())
f.close()
f = open("Hellotxt", "r+")
c = f.write("New Line added")
# content = f.read()
print(c)
f.close()

with open("Hello.txt", "a") as file:
    file.write("my data\n")
    file.write("New Line Data\n")
file.close()