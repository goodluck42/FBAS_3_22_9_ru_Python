# i = 0

# int
# float
# bool
# str
# # i = 5
# while True:
#     print(i)
#
#     i += 1
#
#     if i == 5:
#         break
#
# print("End of loop")

# Outside of continue: 0
# Inside of continue: 1
# Outside of continue: 2


# i = 0 # i = 3
#
# while i < 3:
#     if i == 1:
#         print("Inside of continue:", i)
#         i += 1
#         continue
#
#     print("Outside of continue:", i)
#
#     i += 1
#
# print("End")

#       j0 j1 j2
#  i0  [0, 1, 5]
#  i1  [3, 7, 9]
#  i2  [8, 2, 3]


# matrix = [
#     [0, 1, 5],
#     [3, 7, 9],
#     [8, 2, 3]
# ]
#
# i = 0
# while i < len(matrix):
#     j = 0
#
#     while j < len(matrix[i]):
#         print(f"{matrix[i][j]} ", end="")
#
#         j += 1
#
#     i += 1
#     print()
#
# i = 0

#
# flag = False
# i = 0
#
# while i < 3:
#     j = 0
#
#     while j < 3:
#         if i == 2 and j == 1:
#             flag = True
#             break
#         print("i =", i, "j =", j)
#         j += 1
#
#     if flag:
#         break
#
#     i += 1


# * * * * * * *
# * * * * * * *
# * * * * * * *
# * * * * * * *
# * * * * * * *
# * * * * * * *
i = 0

while i < 7:
    j = 0
    # i - номер строки
    # j - номер столбца
    while j < 9:
        if j == 4 or i == 3:
            print("  ", end="")
            j += 1
            continue

        print("* ", end="")
        j += 1
    print()
    i += 1