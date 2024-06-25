import string


def get_excel_title(n):
    upper_letter = string.ascii_uppercase
    num = [i for i in range(1, len(upper_letter) + 1)]
    my_dict = dict(zip(upper_letter, num))
    for key, value in my_dict.items():
        if n == value:
            print(key)
    print(my_dict)


column_number = 26

get_excel_title(column_number)
