
import random

my_list = []

def generate_ip():
    my_list = []
    oktet1 = random.randrange(0, 256)
    oktet2 = random.randrange(0, 256)
    oktet3 = random.randrange(0, 256)
    oktet4 = random.randrange(0, 256)
    my_list.append(str(oktet1))
    my_list.append(str(oktet2))
    my_list.append(str(oktet3))
    my_list.append(str(oktet4))
    ip = '.'.join(my_list)
    return(ip)


generate_ip()