#List
a = [1, 2,3 ,4,5,6,7,8,9]
print(type(a))
print(a)

#String

a= "hello world!"
b = """hdiashfsdjfsfdjlfj
    kjflksjfsjfslfksf"""
print(a)
print(b)
print(a[10])
# Looping through strings

for x in "hello":
    print(x)

a = "hello"
print(len(a))

# Chexk String

txt = "The Best thing in Life are Trees"
print("free" in txt)
print("Trees" in txt)

# Print only if Trees is present
if "Trees" in txt:
    print("Yes")
else:
    print("No")

b = " Hello, world! "
print(b[8:9])
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace("w", "W"))
print(b.split(','))

# String concatenation
a = "hello "
b = "world"
print(a + b)
print("Hello " + "world")

age = "10"
txt = "My age is " + age
print(txt)
