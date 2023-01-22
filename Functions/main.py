def get_negative_numbers(numbers):
    result = []
    for item in numbers:
        if item < 0:
            result.append(item)

    return result



list1 = [40, -42, -13, 10, 20, -50, 90]
list2 = [42, 10, 20, -19, -13, 45, -72]

result1 = get_negative_numbers(list1)
result2 = get_negative_numbers(list2)

def divide(a=1, b=1, check=True):
    if check and b == 0:
        return "Infinity"
    return a / b


r = divide(20, 5)
r2 = divide(20, 1, False)
r3 = divide()

print(r)
print(r2)
print(r3)
