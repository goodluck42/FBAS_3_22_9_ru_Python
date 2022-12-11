# try:
#     a = int(input("Enter a: "))
#     op = input("Enter op: ")
#     b = int(input("Enter b: "))
#
#     if op == "/":
#         if b != 0:
#             print(a / b)
#         else:
#             print("failed to divide by zero")
#     elif op == "+":
#         print(a + b)
#     else:
#         print("Incorrect operation")
# except:
#     print("An error occurred")


# try:
#     a = int(input("Enter a: "))
#     op = input("Enter op: ")
#     b = int(input("Enter b: "))
#
#     if op == "/":
#         print(a / b)
#     elif op == "+":
#         print(a + b)
#     else:
#         print("Incorrect operation")
# except ValueError as message:
#     print(message)
# except ZeroDivisionError as message:
#     print(message)


value = 42
foo = None

if value > 0:
    foo = 13

if value < 0:
    foo = 130


print(foo)

if foo == None:
    print("foo is none")

print("Hello world")


a = 52
b = 42

if a > 0:
    print("positive")
elif a < 0:
    pass
else:
    print("equals")