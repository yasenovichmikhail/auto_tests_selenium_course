

def restrict_word(s):
    alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    string = s + ' запретил букву'
    for i in range(len(alpha)):
        if len(string) > 0:
            digit = alpha[i]
            if digit in string:
                print(string, digit)
                string = string.replace(digit, "").strip()
                string = string.replace("  ", " ")
            else:
                continue
        else:
            break

s = 'роскомнадзор'

restrict_word(s)