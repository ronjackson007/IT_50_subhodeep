# WAP to Find Largest Number among 3 Numbers

a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

if a > b and a > c:
    print("a = ", a," is Largest")
elif b > a and b > c:
    print("b = ", b," is Largest")
elif c > a and c > b:
    print("c = ", c,"  is Largest")
else:
    print("All are Equal")

# Enter 1st number: 44
# Enter 2nd number: 5
# Enter 3rd number: 55
# c =  55.0   is Largest
