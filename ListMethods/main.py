import random
from random import randint



# numbers = [randint(-100, 100) for i in range(10)]  # list comprehension

# for i in range(10):
#     numbers.append(randint(-100, 100))

## APPEND

# numbers = []
#
# print("len before =", len(numbers))
#
# numbers.append(-100)
#
# print("len after =", len(numbers))
#
# print(numbers)

## POP & REMOVE

#          0   1    2   3     4
# numbers = [42, 13, -10, -10, 99, 90, 1300, 42, 51, 42, 90]
#
# numbers.pop(3)
# numbers.pop()
#
# print("after pop =", numbers)
#
# numbers.remove(42)

## Error handling
# try:
#     numbers.remove(1300)
# except ValueError:
#     print("value not in list")
## EXAMPLE
# books = ["Book1", "Book2", "Book3"]
#
# books.remove("Book2")
# print(books)

# value = 1300
#
# if value in numbers:
#     numbers.remove(value)
# else:
#     print(value, "not found")
#
# print("after remove =", numbers)

## CLEAR

# numbers = [2, 5, 10, 16]
#
# numbers.clear()
#
# numbers.append(42)
#
# print(numbers)


## SORT

# numbers = [randint(-50, 50) for i in range(10)]
#
# print("before sort =", numbers)
#
# # numbers.sort(reverse=True)  # descending
# numbers.sort()  # ascending
#
#
# print("after sort =", numbers)

## SORTED

# numbers = [randint(-50, 50) for i in range(10)]
#
# sorted_list = sorted(numbers)
#
# print(sorted_list)

## COPY

# numbers = [10, 42, 13, 16]
#
# numbers_copy = numbers.copy()
#
# numbers_copy.append(1337)
#
# print("original =", numbers)
# print("copy =", numbers_copy)

## EXTEND

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
#
# list1.extend(list2)
#
#
# print(list1)
#
# list3 = list1 + list2
#
# print(list3)

## INDEX

# numbers = [42, 13, 10, 12, 16]
#
# value = 13
#
# try:
#     idx = numbers.index(value)
#     numbers[idx] = 1337
#
#     print(numbers)
#     print("index of 13 =", idx)
# except ValueError:
#     print("value not in list")

## REVERSE

# numbers = [10, 13, 20, 30, 40, 42]
#
# numbers.reverse()
#
# print("after reverse =", numbers)

## INSERT

# numbers = [42, 13, 10, 90]
#
# #              index, value
# numbers.insert(0, 50)
# numbers.insert(3, 20)
#
# # 50 42, 13, 20, 10, 90
#
# print("after insert =", numbers)


## COUNT

# numbers = [42, 13, 42, 90, 10, 51, 62]
#
# count = numbers.count(99)
#
# print("42 count is =", count)

#######################

## INDEXES & SLICES


numbers = [10, 13, 42, 10, 90, 66, 10, 90]

print(numbers[len(numbers) - 1])  # LAST ELEMENT IN LIST
print(numbers[-1])  # LAST ELEMENT IN LIST
print(numbers[-2])


slice1 = numbers[2:4 + 1]  # SLICE

print(slice1)


slice2 = numbers[::2]

print(slice2)

slice3 = numbers[2:]

print(slice3)

slice4 = numbers[:4]

print(slice4)

slice5 = numbers[:]

print(slice5)

slice6 = numbers[::-1]

print(slice6)


