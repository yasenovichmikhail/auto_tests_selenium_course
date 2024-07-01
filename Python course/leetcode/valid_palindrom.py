import string


def is_valid_palindrim(s):
    char = string.punctuation
    lower_str = s.lower()
    for i in lower_str:
        if i in char:
            lower_str = lower_str.replace(i, '')
        elif i == ' ':
            lower_str = lower_str.replace(' ', '')
    if lower_str == lower_str[::-1]:
        return True
    else:
        return False


s = "A man, a plan, a canal: Panama"
print(is_valid_palindrim(s))
