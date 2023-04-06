

def get_hack_fridge(s):
    list_of_characters = []
    my_string = s
    result = ""
    name = 'anton'
    for i in s:
        list_of_characters.append(i)
    index_a = s.find('a')
    if index_a != -1:
        my_string = my_string[index_a+1:]
        result += 'a'
    
    index_n = my_string.find('n')
    if index_n != -1:
        my_string = my_string[index_n+1:]
        result += "n"
    
    index_t = my_string.find('t')
    if index_t != -1:
        my_string = my_string[index_t+1:]
        result += "t"
    
    index_o = my_string.find('o')
    if index_o != -1:
        my_string = my_string[index_o+1:]
        result += "o"
    
    index_2n = my_string.find('n')
    if index_2n != -1:
        my_string = my_string[index_2n+1:]
        result += "n"
    
    if name == result:
        return True
    else:
        return False

n = int(input())
answer = []
for i in range(n):
    s = input()
    if get_hack_fridge(s) == True:
        answer.append(i + 1)
print(*answer)