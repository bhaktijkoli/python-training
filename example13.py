# To find a factorial of a number
# 5! = 5 * 4 * 3 * 2 * 1

# fact(5) = 5 * fact(4)
# fact(4) = 4 * fact(3)
# fact(3) = 3 * fact(2)
# fact(2) = 2 * fact(1)
# fact(1) = 1

# fact(5) = 5 * 4 * 3 * 2 * 1

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

n = 5
result = fact(n)
print(result)