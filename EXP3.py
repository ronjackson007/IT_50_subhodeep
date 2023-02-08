# Create a list and perform the following methods
# 1) Insert to List
# 2) remove from List
# 3) append to List
# 4) Length
# 5) pop
# 6) clear

l = [1, 2, 'a', 'b', 'c', 50, '+', 'BIT', 'IT']
print(l)

# print('''
# Choose From Following Operations:
#  1) Insert
#  2) remove
#  3) append
#  4) Length
#  5) pop
#  6) clear
# ''')
# ch = int(input('Enter Your Choice: '))
# if ch == 1:
#     i = input("Enter The Element You Want to Insert: ")
#     loc = int(input("At Which Positionc: "))
#     l.insert(loc,i)
#     print(l)
# Insert
print("Insert...")
a = 'a'
l.insert(2, a)
print(l)
# Remove
print("Remove...")
l.remove(2)
print(l)
# append
print("append...")
l.append(100)
print(l)
# Length
print("Length...")
print(len(l))
# pop
print("pop...")
l.pop()
print(l)
# clear
print("clear...")
l.clear()
print(l)

