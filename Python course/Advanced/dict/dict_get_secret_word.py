
def get_secret_word(s, n):
    result = {}
    result1 = {}
    answer = []
    for i in range(len(s)):
        result[s[i]] = result.get(s[i], 0) + 1
    for j in range(n):
        lst = input().split(': ')
        result1[lst[0]] = result1.get(lst[0], int(lst[1]))
    for k in range(len(s)):
        for key, value in result.items():
            for key1, value1 in result1.items():
                if s[k] == key:
                    if value == value1:
                        answer.append(key1)
    print(*answer, sep='')

s = input()
n = int(input())

get_secret_word(s, n)