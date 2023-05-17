
def is_anagrama(s1, s2):
    result = {}
    result1 = {}
    for i in range(len(s1)):
        result[s1[i]] = result.get(s1[i], 0) + 1
    for j in range(len(s2)):
        result1[s2[j]] = result1.get(s2[j], 0) + 1
    print(result)
    print(result1)

    if result == result1:
        print('YES')
    else:
        print('NO')


s1 = 'thing'
s2 = 'night'

is_anagrama(s1, s2)