

def get_unique_words_by_len(sentence):

    lower_words = sentence.lower()
    str_result = ''
    for i in range(len(lower_words)):
        if lower_words[i] not in ('.,;:!?-()'):
            str_result += lower_words[i]

    unique_words = str_result.split(' ')
    my_list = []
    for i in unique_words:
        if len(i) < 4:
            my_list.append(i)
    my_set = set(my_list)
    print(*sorted(my_set))

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

get_unique_words_by_len(sentence)