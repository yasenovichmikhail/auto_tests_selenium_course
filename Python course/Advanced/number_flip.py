

def number_flip(n):
    if len(n) <= 5:
        print(int(n[::-1]))
    else:
        print(n[0] + n[-1:-6:-1])

n = '25000'

number_flip(n)