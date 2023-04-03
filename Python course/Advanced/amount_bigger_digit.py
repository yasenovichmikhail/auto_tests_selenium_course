
def amount_bigger_digit(s):
    list = s.split()
    y = int(list[0])
    counter = 0
    for i in range(len(list)):
        x = int(list[i])
        if x > y:
            counter += 1
            y = x
        elif x <= y:
            y = x
            continue
    print(counter)



s = '1 2 6 2 5'

amount_bigger_digit(s)