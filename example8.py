for i in range(5):
    for j in range(i+1):
        print(i+1, end=" ")

    print()

print("The python way...")
for i in range(5):
    print(str(str(i+1) + " ") * int(i+1))