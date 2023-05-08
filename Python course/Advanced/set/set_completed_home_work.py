def get_amount_of_students(n, m, k, p):

    only_light = k - p
    only_dog = m - p
    all_completed = n - (only_dog + only_light + p)
    print(all_completed)

n = 35  # Всего школьников
m = 20  # Домашнее задание  съела собака
k = 10  # Отключили свет
p = 3  # m & k

get_amount_of_students(n, m, k, p)