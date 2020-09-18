def checkPrime(x):
    for i in range(2, x):
        if x % i == 0:
            print("Not a prime number")
            break;
    else:
        print("Print number")

x = int(input("Enter any number\n"))
checkPrime(x)