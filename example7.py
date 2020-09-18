for i in range(5):
    for j in range(5-i):
        print("X", end=" ")

    print()

for i in range(5):
    print("X " * int(5-i))