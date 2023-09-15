with open('C:/lines.txt', encoding='utf-8') as file:
    content = list(map(lambda st: st.strip(), file.readlines()))
    num = len(max(content, key=len))
    print(num)
    print(*filter(lambda st: len(st) == num, content), sep='\n')