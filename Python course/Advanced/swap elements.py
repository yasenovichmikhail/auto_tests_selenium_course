

def swap_elements(s):
    list = s.split()
    for i in range(0, len(list) - 1, 2):
        list[i], list[i+1] = list[i+1], list[i]
    print(*list) 


s = '2 3 2 4'

swap_elements(s)


