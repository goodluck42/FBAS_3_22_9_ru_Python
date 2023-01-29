import my_math as mm
from my_math import divide, multiply as mult

# from my_math import *
# from random import *

while True:
    num1 = float(input("Enter num1 -> "))
    op = input("Enter op -> ")
    num2 = float(input("Enter num2 -> "))

    if op == "+":
        result = mm.add(num1, num2)

        print(result)
    elif op == "-":
        pass
    elif op == "*":
        result = mult(num1, num2)

        print(result)
    elif op == "/":
        result = divide(num1, num2)

        print(result)
    else:
        print("Incorrect input")
