
def get_packaging_of_duplicates(s):
    list = s.split(' ')
    result = [[]]
    print(list)
    for i in range(len(list)):
        if [list[i]] not in result:
            result.append([list[i]])
        else:
            while [list[i]] == result[-1]:
                print([list[i]])
                print(result[-1])
                result[-1].append(list[i])
                # print(result[-1])
                print(result)


s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'

get_packaging_of_duplicates(s)