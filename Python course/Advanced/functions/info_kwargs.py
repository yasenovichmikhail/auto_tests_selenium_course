def info_kwargs(**kwargs):
    lst = sorted(kwargs)
    for j in lst:
        for key, value in kwargs.items():
            if j == key:
                print(f'{key}: {value}')

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 