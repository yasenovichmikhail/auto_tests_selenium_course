import random

def get_secret_friend():
    s = [input() for _ in range(int(input()))]
    print(s)
    counter = 0
    result_list = []
    while counter != len(s):
        for i in s:
            x = random.choice(s)
            print(x)
            print(i)
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
#    print(result_list)    
    for k in result_list:
        print(f"{k[0]} - {k[1]}")
        
                
get_secret_friend()