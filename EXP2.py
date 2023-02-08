# WAP to Find Largest Number among 3 Numbers

a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

if a > b and a > c:
    res = a
elif b > a and b > c:
    res = b
elif c > a and c > b:
    res = c
else:
    print("All are Equal")
print("Largest Number is ", float(res))
# Enter 1st number: 44
# Enter 2nd number: 5
# Enter 3rd number: 55
# c =  55.0   is Largest

# Enter 1st number: 222
# Enter 2nd number: 44
# Enter 3rd number: 44
# Largest Number is  222.0