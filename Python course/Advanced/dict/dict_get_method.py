
def get_method(numbers):
    numbers = [i for i in range(1, 16)]
    result = {}
    for num in numbers:
        result[num] = result.get(num, num ** 2)
    print(result)

numbers = [i for i in range(1, 16)]

get_method(numbers)