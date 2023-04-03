



def get_points(z):
    x = z.split()
    quater1 = 0
    quater2 = 0
    quater3 = 0
    quater4 = 0
    if int(x[0]) < 0 and int(x[1]) > 0:
        quater2 += 1
    elif int(x[0]) > 0 and int(x[1]) < 0:
        quater4 += 1
    elif int(x[0]) < 0 and int(x[1]) < 0:
        quater3 += 1
    elif int(x[0]) > 0 and int(x[1]) > 0:
        quater1 += 1

    print('Первая четверть:', quater1)
    print('Вторая четверть:', quater2)
    print('Третья четверть:', quater3)
    print('Четвертая четверть:', quater4)

z = '1 2'

get_points(z)