# assignment operator

a = 42

a = a + 5


# shorthand operators (assignment operators)
a += 5

a -= 7

a /= 2

a //= 2

a **= 2

a %= 10

a *= 2

# print(a)

# arithmetic operators

# +, -, *, /, //, %, **

# comparison operators

# x = 42
# y = 13
#
# print("x =", x)
# print("y =", y)
# print("x > y :", x > y)
# print("x < y :", x < y)
# print("x >= y :", x >= y)
# print("x >= y :", x <= y)
# print("x >= y :", x == y)


# age program
# age = int(input())
#
# if age >= 18:
#     print("You are allowed")
# else:
#     print("You are not allowed")

age = int(input())

if age < 20:
    print("You are teenager")
elif age >= 20:
    print("You are a student")
elif age >= 60:
    print("You are a retired")
else:
    print("You are very old person")

if age == 42:
    print("You are 42 years old")
