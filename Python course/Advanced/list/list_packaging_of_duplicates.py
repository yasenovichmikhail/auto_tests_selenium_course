res = []

def get_packaging_of_duplicates(s):
    s = s.split()
    for el in s:
        if res and el in res[-1]:
            res[-1].append(el)
        else:
            res.append([el])

    print(res)


s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'

get_packaging_of_duplicates(s)