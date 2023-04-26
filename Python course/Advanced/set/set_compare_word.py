a = 'автор товар отвар'
list = a.split(' ')
word1 = list[0]
word2 = list[1]
word3 = list[2]

set_word1 = set(word1)
set_word2 = set(word2)
set_word3 = set(word3)
if set_word1 == set_word2 == set_word3:
    print('YES')
else:
    print('NO')