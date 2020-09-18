p = 3
n = 1
for i in range(4):
    for j in range(7):
        if j >= p and j <= p+n-1:
            print("X", end=" ")
        else:
            print(" ", end=" ")

    print()
    p -= 1
    n += 2

print("The python string multiplication way")
p = 3
n = 1
for i in range(4):
    print("  " * p, end="")
    print("X " * n, end="")
    print()
    p -= 1
    n += 2