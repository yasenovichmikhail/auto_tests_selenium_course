with open(input(), encoding='utf-8') as file:
    print(*file.readlines()[-10:], sep='')