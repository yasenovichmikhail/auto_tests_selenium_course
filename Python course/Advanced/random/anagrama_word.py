
import random

def get_anagrama(word):
    lst = [word[i] for i in range(len(word))]
    random.shuffle(lst)
    s = ''
    for j in range(len(lst)):
        s += str(lst[j])
    print(s)
    
word = 'липа'

get_anagrama(word)