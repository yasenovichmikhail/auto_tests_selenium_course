# объявление функции
def get_month(language, number):
    lng_ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    lng_en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru' and number == 1:
        return lng_ru[1]
    elif language == 'ru' and number == 2:
        return lng_ru[2]
    elif language == 'ru' and number == 3:
        return lng_ru[3]
    elif language == 'ru' and number == 4:
        return lng_ru[4]
    elif language == 'ru' and number == 5:
        return lng_ru[5]
    elif language == 'ru' and number == 6:
        return lng_ru[6]
    elif language == 'ru' and number == 7:
        return lng_ru[7]
    elif language == 'ru' and number == 8:
        return lng_ru[8]
    elif language == 'ru' and number == 9:
        return lng_ru[9]
    elif language == 'ru' and number == 10:
        return lng_ru[10]
    elif language == 'ru' and number == 11:
        return lng_ru[11]
    elif language == 'ru' and number == 12:
        return lng_ru[12]
    elif language == 'en' and number == 1:
        return lng_en[1]
    elif language == 'en' and number == 2:
        return lng_en[2]
    elif language == 'en' and number == 3:
        return lng_en[3]
    elif language == 'en' and number == 4:
        return lng_en[4]
    elif language == 'en' and number == 5:
        return lng_en[5]
    elif language == 'en' and number == 6:
        return lng_en[6]
    elif language == 'en' and number == 7:
        return lng_en[7]
    elif language == 'en' and number == 8:
        return lng_en[8]
    elif language == 'en' and number == 9:
        return lng_en[9]
    elif language == 'en' and number == 10:
        return lng_en[10]
    elif language == 'en' and number == 11:
        return lng_en[11]
    elif language == 'en' and number == 12:
        return lng_en[12]

# считываем данные
lan = 'en'
num = 6

# вызываем функцию
print(get_month(lan, num))