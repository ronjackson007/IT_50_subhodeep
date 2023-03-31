# WAP to compute the  number of char, words and lines in a file
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
print("No. of Char: ",len(d))
for line in con:
    # content = line.split
    if line in d2:
        d2[line] = d2[line] + 1
    else:
        d2[line] = 1
print("No. of Words: ",len(d2))
print("No. of Lines: ",len(content.split("\n")))
# OUTPUT
# No. of Char:  13
# No. of Words:  5
# No. of Lines:  3
