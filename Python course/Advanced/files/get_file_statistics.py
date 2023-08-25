with open('C:/file.txt', encoding='utf-8') as file:
    counter_letter = 0
    counter_lines = 0
    counter_words = 0
    for i in file:
        x = i.split()
        counter_words += len(x)
        counter_lines += 1
        for j in i:
            if j.isalpha():
                counter_letter += 1
    print('Input file contains:')
    print(f'{counter_letter} letters')
    print(f'{counter_words} words')
    print(f'{counter_lines} lines')