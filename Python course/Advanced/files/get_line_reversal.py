with open('text.txt', encoding='utf-8') as file:
    x = file.readline().strip()
    print(x[::-1])