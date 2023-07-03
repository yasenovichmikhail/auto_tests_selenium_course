def pretty_print(*args, side='-', delimiter='|'):
    stroka = f' {delimiter} '.join(map(str, args))
    print('', (len(stroka) + 2) * side)
    print(delimiter, stroka, delimiter)
    print('', (len(stroka) + 2) * side)

pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')