# list
# int
# float

# students = ["Jafar", "Ayhan", "Ibrahim", "Murad"]
#
# for i in range(len(students)):
#     students[i] += " Surname"
#
# print(students)

################################################
# #              0        1         2         3
# students = ["Jafar", "Ayhan", "Ibrahim", "Murad"]
#
# index = 2
#
# print(students[index])
#
# students[index] = "Iosif"
#
# print(students)
#
# good_list = [1, 2, 3, 4, 42]
# bad_list = ["Vadim", 42, True, 42.13]
# good_tuple = ("Vadim", 22)

#######################################
## Random number №1

# from random import randint
#
# x = randint(-100, 100)
#
# print(x)


## Random number №2

# import random
#
# x = random.randint(-100, 100)
#
# print(x)

#################################################

# List length

#          0   1   2   3   4
# numbers = [12, 55, 42, 13, 99]

# FAKE
# for i in numbers:
#     i *= 2
#
# print(numbers)

## REAL

# size = len(numbers)

# print("SIZE =", size)

## FOR VARIANT
# for i in range(len(numbers)):  # 0 1 2 3 4
#     numbers[i] *= 2

## WHILE VARIANT

# i = 0
#
# while i < len(numbers):
#     numbers[i] *= 2
#     i += 1

# print(numbers)

#############################
## APPEND

from random import randint

numbers = []  # list

x = 13  # int

# y = int(input())
numbers.append(42)
# numbers.append(y)
numbers.append(x)

for i in range(10):
    rnd = randint(-10, 10)
    # numbers.append(rnd)

    numbers.append(randint(-10, 10))

print(numbers)
