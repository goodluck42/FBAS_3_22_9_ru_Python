import random

# # break
# base_id = 0
# max_id = 10000
# target_id = int(input())  # 400
#
# while base_id < max_id:
#     if base_id == target_id:
#         print("User found")
#         break
#
#     base_id += 1
# import random

# # do not do that
# i = 0
#
# while i < 5:
#     print(i)
#     i += 1
#     break

# # Random1
# from random import randint
#
# random_number = randint(1, 100)
#
# print(random_number)


# # Random2
# import random
#
# random_number = random.randint(1, 100)
#
# print(random_number)


# # continue
# base_id = 0
# max_id = 10
#
# while base_id < max_id:
#     age = random.randint(12, 48)
#
#     if age < 18:
#         print("Age", age, "not allowed")
#
#         base_id += 1
#         continue
#
#     print("Age", age, "allowed")
#
#     base_id += 1


# i = 0
#
# while i < 10:
#     if i >= 2 and i <= 5:
#         i += 1
#         continue
#
#     print(i)
#     i += 1


# # Flags
#
# base_id = 0
# max_id = 10000
# target_id = int(input())  # 400
# found = False
#
# while base_id < max_id:
#     if base_id == target_id:
#         found = True
#         break
#
#     base_id += 1
#
# # do not do that
# # found == True
# if found:
#     print("User found")
# else:
#     print("User not found")


while True:
    a = int(input())
    op = input()
    b = int(input())
    result = None

    if op == "+":
        result = a + b

    if op == "0":
        continue

    print(result)
