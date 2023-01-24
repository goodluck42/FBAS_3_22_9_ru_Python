def create_student(**kwargs):
    age = kwargs["age"]

    if age < 16 or age > 100:
        raise ValueError("Invalid age")

    student = {
        "name": kwargs["name"],
        "surname": kwargs["surname"],
        "age": age
    }

    return student

try:
    create_student(name="Vadim", surname="Siga", age=999)
except ValueError as message:
    print(message)

# list1 = [20, 30, 40]
#
# student = {
#     "name": "Vadim",
#     "age": 20
# }
#
# tuple1 = ("name", "Vadim")
# tuple2 = ("age", 20)
# ##########################
# def my_sum(*args, num):
#     _sum = 0
#
#     for item in args:
#         _sum += item
#
#     return _sum
#
#
# result = my_sum(1, 2, 3, 4, 5, 6, 10, 20, num=42)
#
# print(result)


# f = []  # [10, 20, 30]
#
# def change(value):
#     # value = f
#     value.extend([10, 20, 30])
#
# change(f)
#
# print(f)


# value = 42
# str, bool, int, float, tuple
# def fn():
#     global value
#     value += 10
#
# fn()
#
# print(value)
######################
# list1 = []
#
# def fn2():
#     list1.append(10)
#     list1.append(42)
#     list1.append(13)
#
# fn2()
######################
# print(list1)

# def get_average(numbers):
#     _sum = 0  # local variable
#
#     for item in numbers:
#         _sum += item
#
#     result = _sum / len(numbers)
#
#     return result
#
# list1 = [1, 2, 3]
#
# print(get_average(list1))

#
# a = int(input())
#
# result = None
#
# if a > 0:
#     result = 42
#
# print(result)



# def find_average(numbers):
#     _sum = 0
#
#     for item in numbers:
#         _sum += item
#
#     result = _sum / len(numbers)
#
#     return result
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]
#
# avg1 = find_average(list1)
# avg2 = find_average(list2)
#
# print(avg1)
# print(avg2)