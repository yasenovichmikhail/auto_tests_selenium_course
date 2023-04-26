def get_amount_of_students(n, m, k, x, y, z, t, a):

    first_or_second = n + m
    second_or_third = m + k
    third_or_first = n + k
    first_and_second = first_or_second - x
    second_and_third = second_or_third - y
    third_and_first = third_or_first - z

    # Находим количество студентов, которые прочитали 1 & 2, 2 & 3, 3 & 1
    x1 = first_and_second - t
    x2 = second_and_third - t
    x3 = third_and_first - t

    # Находим количество студентов, которые прочитали одну книгу
    one_book = (n - (x1 + x3 + t)) + (m - (x1 + x2 + t)) + (k - (x2 + x3 + t))

    # Находим количество студентов, которые прочитали две книги
    two_book = x1 + x2 + x3

    # Находим количество студентов, которые не прочитали ни одной книги
    none_book = a - t - one_book - two_book
    return print(one_book, two_book, none_book, sep='\n')

n = 19  # "Что такое математика?"
m = 18  # "Математическая составляющая"
k = 22  # "100 гениальных идей по математике"
x = 32  # ("Что такое математика?" | "Математическая составляющая") | ( & )
y = 33  # "Математическая составляющая" | "100 гениальных идей по математике" | ( & )
z = 35  # "Что такое математика?" | "100 гениальных идей по математике" | ( | )
t = 2   # Полностью выполнили задание
a = 50  # Всего учеников

get_amount_of_students(n, m, k, x, y, z, t, a)
