# name surname age grades
# dict
# student = {
#     "name": "Иосиф",
#     "surname": "Юсубов",
#     "age": 17,
#     "grades": [12, 7, 9, 10]
# }
# student2 = {
#     "name": "Джафар",
#     "surname": "Джафаров",
#     "age": 15,
# }
#
# students = []
#
# students.append(student)
# students.append(student2)
#
# print(f"all students = {students}")
#
# print(students[1]["name"])

#####################

student = {
    "name": "Айхан",
    "surname": "Хагвердиев",
    "age": 15,
    "grades": [12, 7, 9, 10]
}

student["age"] += 1
student["group_name"] = "FBAS_3_22_9_ru"

print(student)


## POP

student.pop("grades")

print(f"{student} (after pop)")

## KEYS & VALUES

keys = student.keys()

print(f"keys = {list(keys)}")

values = student.values()

print(f"values = {list(values)}")

## ITEMS

for k, v in student.items():
    print(f"key = {k}\nvalue = {v}")


def fn(*args, **kwargs):
    print(args[0])
    print(kwargs["key"])

fn(1, 4, 5, 6, 8, 9, key="helloy")

x = filter(lambda v: v > 0, [1, -2, 3, 4, 5, 6])

print(list(x))