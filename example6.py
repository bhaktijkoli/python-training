samples = (1, 2, 3, 4, 12, 5, 20, 11, 21)
e = o = 0
for s in samples:
    if s % 2 == 0:
        e += 1
    else:
        o += 1

print("Number of even numbers : %d" % (e))
print("Number of odd numbers : %d" % (o))