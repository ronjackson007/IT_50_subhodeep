#creating Variable
from doctest import Example

x = 55
#print(x)
y = "Hello"

print(y, x)

#DataType Casting
x = int(5)
print(x)
print(str(x))
print(float(x))

# Gettype
var1 = 55
var2 = "Hello"
var3 = 2.06
print(type(var1))
print(type(var2))
print(type(var3))

# SingleDoubleQuotes
x = 'Hello'
print(x)
x = "Hello"
print(x)
x = '''Hello
World
'''
print(x)

# CaseSensitive
a = 5
A = 'DATE'
print(a, A)

# AssignMultipleValues
x, y, z = "Hello", "BIT", "DURG"
print(x, y, z)

# OneValueMultipleVaariable
x=y=z = "Hello"
print(x, y, z)

# GlobalVariable
B = 55
def my_function():
    print("My age is: ",B)
my_function()
# Example
c1 = 33
def my_fun():
    c2 = 44
    print(10 + c1)
    print(10 + c2)
my_fun()
print(5 + c1)