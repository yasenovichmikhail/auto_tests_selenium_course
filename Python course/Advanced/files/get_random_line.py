
import random

file_name = 'C:/languages.txt'
def get_random_line(file_name):
    file = open(file_name, encoding='utf-8')
    content = [i.rstrip() for i in file.readlines()]
    x = random.sample(content, 1)
    print(*x)
    file.close()

get_random_line(file_name)