"""
num1 = int(input("First Number:"))
num2 = int(input("Second Number:"))

changenum = num1
num1 = num2
num2 = changenum

print("\nChanged Number 1:",num1)
print("Changed Number 2:",num2)
"""

num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))

print("Before the change\nNumber1: {}\nNumber2: {}\n".format(num1,num2))
num1,num2 = num2,num1

print("After the change\nNumber1: {}\nNumber2: {}".format(num1,num2))