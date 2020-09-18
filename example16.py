def is_leap(y):
    return y % 4 == 0

y = int(input("Enter a year\n"))
if is_leap(y):
    print("Leap year")
else:
    print("Not a Leap Year")