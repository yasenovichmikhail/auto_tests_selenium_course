
def get_zodiac(year):
    list_of_year = []
    list = [' ', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна']
    for i in range(year, 0, -12):
        list_of_year.append(i)
    return print(list[list_of_year[-1]])

year = 1945

get_zodiac(year)



