n = '10000000'

str_len = len(n)
set_len = len(set(n))

if str_len == set_len:
    print('YES')
elif str_len != set_len:
    print('NO')
else:
    print('Something went wrong')