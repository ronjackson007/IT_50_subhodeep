# 11. Write a Program to check weather the given string is palindrome

# def isPlaindrome(num):
#     num = int(input("Please Enter a number"))
#     flag = num
#     num1 = str(num)
#     res = 0
#     while(num > 0):
#         dig = num % 10
#         res = res * 10 + dig
#         num = num // 10
#     if flag == res:
#         print("Palindrome")
#     else:
#         print("Not Plaindrome")
# isPlaindrome(232)

def sPalindrome():
    str = input("Enter a String: ")
    rev_string = str[::-1]
    if rev_string == str:
        print("Palindrome")
    else:
        print("Not Plaindrome")
sPalindrome()