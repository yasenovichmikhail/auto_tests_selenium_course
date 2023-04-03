def get_amount(s):
    t=0
    while "Р"*(t+1) in s:
        t+=1
    print(t)
s = 'ОРРОРОРООРРРPPPО'

get_amount(s)