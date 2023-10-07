with open(input(), encoding='utf-8') as words_file, open('forbidden_words.txt', encoding='utf-8') as forbidden_file:
    forbidden_words = forbidden_file.read().split()
    for i in words_file:
        for j in forbidden_words:
            while j in i.lower():
                index = i.lower().index(j)
                i = i[:index] + '*' * len(j) + i[index + len(j):]
        print(i.strip())