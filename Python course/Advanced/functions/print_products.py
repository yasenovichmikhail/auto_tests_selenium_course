def print_products(*args):
    lst = [i for i in args if type(i) == str and len(i) > 0]
    for k in range(len(lst)):
        if len(lst) > 0:
            print(f"{k + 1}) {lst[k]}")
    if len(lst) == 0:
        print('Нет продуктов')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)