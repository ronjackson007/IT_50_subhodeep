# Creating Python functions
a = 10
b = 20
c = sum((a, b))
print(c)

# User defined functions
def myfunc(): #Function declaration
    print("This is a user defined function")
myfunc() #Function calling

def my_algo():
    print("step 1 ^-^")
    print("step 2 ^-^")
    print("step 3 ^-^")
    print("step 4 ^-^")
my_algo()
my_algo()
my_algo()
my_algo()

# Accepts values in function through argument or parameter

# 1
def myfun2(fname):
    print(fname + " 0.0")
myfun2("ABC")
myfun2("123")
myfun2("XYZ")

# If th enumber of argumes are unknown, add a * before parameter name

def myfun3(*key):
    print(key[0])
myfun3('abc', 'xyz')

# Default parameters value
def myfun4(city = 'Bhilai'):
    print("City is " + city)
myfun4()
myfun4("Durg")

# Passing a list as Argument
def myfun5(list1):
    for x in list1:
        print(x)
list1 = ['abc', 'xyz','123','lkj']
myfun5(list1)

# Return Value
def myfun6(x):
    return x**2
c = myfun6(4)
print(c)

#To Pass function
def myfun7():
    pass

# Recursion function


