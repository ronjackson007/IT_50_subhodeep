# The While Loop
i = 0
while i<7:
    print(i, end="  ")
    i+=1
#   i = i + 1
i = 0
while(True):
    print(i)
    i = i + 1
    if i == 3:
        break

i = 0
while i < 7:
    i += 1
    # print(i)
    if i <= 6:
        continue
print(i)
# The Else statement
# wHILE ELSE

i = 1
while i < 6:
    print(i)
    i+=1
else:
    print("i IS NO LONGER LESS THAN 6")

# ForLOop
# Print Each fri=uit in a fruirt list

fruit = [['apple', 2], ['banana', 5], ['orange', 6], ['cherry', 10]]
for x, kg in fruit:
    print(x, kg)

dist1 = dict(fruit)
# print(dist1)

for x, qt in dist1.items():
    print(x ,qt)

for x in "banana":
    print(x)

fruit = ['apple', 'banana', 'orange']
for x in fruit:
    print(x)
    if x == 'banana':
        break