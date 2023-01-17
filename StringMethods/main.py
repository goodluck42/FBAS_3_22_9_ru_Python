# # MENU
# while True:
#     print("1. New game")
#     print("2. Load game")
#     print("3. Settings")
#     print("4. Exit")
#
#     option = int(input())
#
#     if option == 1:
#         print("Starting new game")
#     elif option == 2:
#         print("Loading game")
#     elif option == 3:
#         print("Entering settings")
#     elif option == 4:
#         break
#     else:
#         print("Incorrect command")


## UPPER & LOWER
# text = "Hello world"
#
# upper_text = text.upper()
# lower_text = text.lower()
#
# print(upper_text, lower_text)

# # IS METHODS
# text = "1A"

# print(text.isalpha())
# print(text.isdigit())
# print(text.isascii())
# print(text.isalnum())
# print(text.islower())
# print(text.isupper())

# # REPLACE

# text = "Hello Iosif"
#
# result = text.replace("Iosif", "Ibrahim")
#
# result = result.replace("l", "0", 1)
#
# print(text)
# print(result)

# # SPLIT & JOIN

# text = "2 + 5 + 42"
#
# result = text.split("+")
#
# print(result)

# _sum = 0

# for value in result:
#     _sum += int(value)
#
# print(_sum)

# join_result = "-".join(result)
#
# print(join_result)

# #

# word1 = "BuS"
# word2 = "bUs"
#
# if word1.lower() == word2.lower():
#     print("Equals")


# # CAPITALIZE
# text = "hello world"
#
# result = text.capitalize()
#
# print(result)


# # SWAPCASE

# text = "Hello worlD"
#
# result = text.swapcase()
#
# print(result)

# # STARTSWITH & ENDSWITH

# text = "helloy."
#
# if text.startswith("H"):
#     print("STARTS")
# else:
#     print("NOT STARTS")
#
# if text.endswith("."):
#     print("ENDS")
# else:
#     print("NOT ENDS")

# # FIND

# text = "hello world"
#
# result = text.find("world")
#
# print(result)

# # STRIP

# text = "       hello my friend     "
#
# clear_text = text.strip()
#
# print(clear_text)

print(eval("2 + 2 * 2 / 2"))