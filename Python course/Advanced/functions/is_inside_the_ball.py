abscissas = '0.0 1.0 2.0'
ordinates = '0.0 0.0 1.1'
applicates = '0.0 1.0 1.5'

def is_inside_the_ball(abscissas, ordinates, applicates):
    bool_lst = []
    abscissas = abscissas.split()
    ordinates = ordinates.split()
    applicates = applicates.split()
    lst_zip = list(zip(abscissas, ordinates, applicates))
    for i in lst_zip:
        if (float(i[0]) ** 2) + (float(i[1]) ** 2) + (float(i[2]) ** 2) <= 4:
            bool_lst.append(True)
        else:
            bool_lst.append(False)
    result = all(bool_lst)
    print(result)

is_inside_the_ball(abscissas, ordinates, applicates)