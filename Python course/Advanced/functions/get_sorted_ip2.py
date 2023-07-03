def dec(IP):
    lst = [int(i) for i in IP.split('.')]
    return lst[0] * 256 ** 3 + lst[1] * 256 ** 2 + lst[2] * 256 + lst[3]
    
print(*sorted([input() for _ in range(int(input()))], key=dec), sep='\n')