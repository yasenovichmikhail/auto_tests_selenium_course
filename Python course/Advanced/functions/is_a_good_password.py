password = input()

def is_a_good_len(password):
    result = any(map(lambda x: len(password) >= 7, password))
    return result

def is_upper_case(pasword):
    result = any(map(lambda x: x.isupper(), password))
    return result

def is_lower_case(pasword):
    result = any(map(lambda x: x.islower(), password))
    return result

def is_digit(pasword):
    result = any(map(lambda x: x.isdigit(), password))
    return result

def is_a_good_password(password):
    if is_a_good_len(password) and is_upper_case(password) and is_lower_case(password) and is_digit(password):
        print('YES')
    else:
        print('NO')

is_a_good_password(password)