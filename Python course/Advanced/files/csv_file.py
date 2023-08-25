def read_csv():
    lst = []
    with open('C:/data.csv') as file:
        my_dict = {}
        keys = file.readline().strip().split(',')
        for k in file:
            line = k.strip().split(',')
            x = dict(zip(keys, line))
            lst.append(x)
    return lst

print(read_csv())