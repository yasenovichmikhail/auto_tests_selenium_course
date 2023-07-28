ip = '10.0.1.1'

def is_letters(ip):
    abc1 = 'zyxwvutsrqponmlkjihgfedcba'
    ABC2 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    for i in abc1:
        if i in ip:
            return False

def is_correct_ip(ip):
    ip_lst = ip.split('.')
    result = all(map(lambda x: True if x.isdigit() and 0 <=int(x) < 256 else False, ip_lst))
    print(result)

is_correct_ip(ip)
# is_letters(ip)