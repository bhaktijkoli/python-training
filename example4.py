x = input("Enter a string \n")
d = l = 0

for c in x:
    if c.isalpha():
        l += 1

    if c.isdigit():
        d += 1;

print("Letters %d" % (l))
print("Digits %d" % (d))