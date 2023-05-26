import random

def get_secret_friend():
    s = [input() for _ in range(int(input()))]
    counter = 0
    result_list = []
    while counter != 3:
        for i in s:
            print(i)
            x = random.choice(s)
            if i != x:
                tmp = [i, x]
                tmp1 = [x, i]
                if tmp not in result_list and tmp1 not in result_list:
                    result_list.append(tmp)
                    counter += 1
#                    print(f"{i} - {x}")
                else:
                    continue
            else:
                continue
    print(result_list)    
    for k in result_list):
        
        
                
get_secret_friend()