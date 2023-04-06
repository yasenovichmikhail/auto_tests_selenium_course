

def swap_elements(s):
    list = s.split()
    list_new = list[-1:] + list[:-1]
    print(*list_new) 


s = '1 2 3 4 5'

swap_elements(s)


