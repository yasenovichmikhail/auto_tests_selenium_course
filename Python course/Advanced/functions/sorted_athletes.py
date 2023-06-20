athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

n = 1

def get_sorted_by_parameter(athletes, num):
    result = sorted(athletes, key=lambda x: x[num-1])
    for i in result:
        print(*i, end='\n')

get_sorted_by_parameter(athletes, n)

