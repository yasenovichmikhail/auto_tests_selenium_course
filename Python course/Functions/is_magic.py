# объявление функции
def is_magic(date):
    list = date.split('.')
    a = int(list[0]) * int(list[1])
    b = int(list[2])%100
    if a == b:
        return True
    else:
        return False

date = '10.06.1960'

# вызываем функцию
print(is_magic(date))