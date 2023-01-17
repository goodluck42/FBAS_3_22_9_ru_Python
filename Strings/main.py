# bool, str, int, float, list

# Изменяемые (mutable), ReferenceType
# list

# Неизменяемые (immutable) ValueType
# int, float, bool, str, tuple

###### ValueType
# a = "Hello"
# b = a

# # print(id(a))
# # print(id(b))


# # a = "World"

# # print(id(a))
# # print(id(b))

# print(b, a)

###### ReferenceType

# a = []
# b = a
# c = b
#
# print(id(a))
# print(id(b))
#
# a.append(13)
# b.append(42)
# c.append(10)
#
# print(a)
# print(b)
# print(c)
#
# x1 = []
# x2 = []
#
# print("ReferenceType = ", hex(id(x1)))
# print("ReferenceType = ", hex(id(x2)))

########
# a = 42
# b = 42
#
# print("ValueType = ", hex(id(a)))
# print("ValueType = ", hex(id(b)))

# text = "HELLO"

# text[0] = 'h'
# print(text[0])

# lower = text.lower()
#
# print(f"text = {text}")
# print(f"lower = {lower}")


## CONCATENATION

# a = "Hello "
# b = "world"
#
# result = a + b
#
# print(result)

## REPLICATION

# result2 = b * 5
#
# print(result2)

### FORMAT

# a = 5
# b = 6
#
# print(a, '*', b, '=', a * b)
#
# print(f"{a} * {b} = {a * b}")


### isalpha & isdigit
# text = "1"
#
# if text.isdigit():
#     print("is digit")
#
# text2 = "T"
#
# if text2.isalpha():
#     print("is alpha")

## STRING ITERATION

# text = "Hello"
#
# for c in text:
#     print(c)
#
# for i in range(len(text)):
#     print(text[i])


## ESCAPE SEQUENCES
# \t - tabulation

# print("Hello\tWorld")
# print("Hello\nWorld")
# print("Hello\\World")
print("Hello\rWorld")

import string

print(string.digits)
print(string.punctuation)