# Write a Program to find multiplication of two numbers using class and object
# class MuL, user input, int type, 3rd attribute resul
class Mul:
    fno = int(input("Enter 1st: "))
    sno = int(input("Enter 2nd: "))
    result = fno * sno

multiply = Mul()
print("Multiplication of ",multiply.fno, "x", multiply.sno, "is", multiply.result)
