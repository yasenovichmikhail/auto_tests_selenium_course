

def convention(n):
    reverse = n[::-1]
    a = reverse[0:3]
    b = reverse[3:6]
    c = reverse[6:9]
    d = reverse[9:12]
    e = reverse[12:15]
    if len(n) <= 8:
        nummmm = a + ',' + b + ',' + c
        return print(nummmm[::-1])
    elif 9<= len(n) <= 11:
        nummmm = a + ',' + b + ',' + c + ',' + d
        return print(nummmm[::-1])

n = '100000000'

convention(n)