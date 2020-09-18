# Password generator
import random as r
lenth = int(input("Enter the length of password\n"))
password = ""
for i in range(lenth):
    password += chr(r.randint(33, 123))

print(password)