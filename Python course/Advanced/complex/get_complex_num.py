def get_complex_num(a, b):
    summa = a + b
    diff = a - b
    multiply = a * b
    print(f"{a} + {b} = {summa}")
    print(f"{a} - {b} = {diff}")
    print(f"{a} * {b} = {multiply}")

a = complex(input())
b = complex(input())

get_complex_num(a, b)