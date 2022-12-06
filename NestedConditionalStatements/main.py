# key = input()

# char
# esc, y, n

# !=

# if key == "esc":
#     print("Exit")
# elif key == "y":
#     print("Command accepted")
# elif key == "n":
#     print("Command declined")
# else:
#     print("Incorrect command")

# + - / // ** % (арифметические)
# = += -= /= *= //= **= (assignment operators)
# > < >= <= == !=

# and
# or
# not

# and
# 1 and 1 => True
# 0 and 1 => False
# 1 and 0 => False
# 0 and 0 => False

# or
# 1 or 1 => True
# 0 or 1 => True
# 1 or 0 => True
# 0 or 0 => False

# not

# not True => False
# not False => True


age = int(input("Enter your age: "))
role = input("Enter your role: ")  # admin, user

if age >= 18 and age <= 100:
    if role == "admin":
        print("admin access granted")
    elif role == "user" or role == "default":
        print("standard access granted")
    else:
        print("invalid role, access denied")
else:
    print("access denied")