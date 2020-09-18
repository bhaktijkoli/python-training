#Write a python program to count the numbers of alphabets, digits and spaces in a file.

f = open("demo.txt", "r")
alphabets = 0
digits = 0
spaces = 0
others = 0
lines = f.readlines()
for line in lines:
    for c in line:
        if c.isalpha():
            alphabets += 1
        elif c.isdigit():
            digits += 1
        elif c.isspace():
            spaces += 1
        else:
            others += 1


print("Number of alphabets", alphabets)
print("Number of digits", digits)
print("Number of spaces", spaces)
print("Others", others)