
def is_anagrama_2(s1, s2):
    s3 = '.,!?:;- ' 
    s1_or = ''
    s2_or = ''
    for i in range(len(s1)):
        if s1[i] not in s3:
            s1_or += s1[i].lower()
    for i in range(len(s2)):
        if s2[i] not in s3:
            s2_or += s2[i].lower()
    result = {}
    result1 = {}
    # print(s1_or)
    # print(s2_or)
    for j in range(len(s1_or)):
        result[s1_or[j]] = result.get(s1_or[j], 0) + 1
    for k in range(len(s2_or)):
        result1[s2_or[k]] = result1.get(s2_or[k], 0) + 1
    # print(result)
    # print(result1)
    
    if result == result1:
        print('YES')
    else:
        print('NO')


s1 = 'William Shakespeare'
s2 = 'I am a weakish: speller,'

is_anagrama_2(s1, s2)