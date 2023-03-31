# WAP to count frequency of character in a given file
fname = open("Hello.txt", 'r')
d = {}
d2 = {}
content = fname.read()
con = content.split(" ")
for line in content:
    # content = line.split
    if line in d:
        d[line] = d[line] + 1
    else:
        d[line] = 1
print(d)
for line in con:
    # content = line.split
    if line in d2:
        d2[line] = d2[line] + 1
    else:
        d2[line] = 1
print(d2)
# OUTPUT
# {'m': 4, 'y': 4, ' ': 5, 'd': 2, 'a': 4, 't': 2, '\n': 2, 'N': 1, 'e': 2, 'w': 1, 'L': 1, 'i': 1, 'n': 1}
# {'my': 2, 'data\nmy': 1, 'my\nNew': 1, 'Line': 1, 'data': 1}