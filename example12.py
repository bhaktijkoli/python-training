# 0 1 1 2 3 5 8
def fib(n):
    a = 0
    b = 1
    print(a, end=" ")
    print(b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

n = int(input("Enter the number\n"))
fib(n)