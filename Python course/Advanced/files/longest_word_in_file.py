with open('words.txt', encoding='utf-8') as file:
    lst = file.read().split()
    print(*[i for i in lst if len(i) == len(max(lst, key=len))], sep='\n')