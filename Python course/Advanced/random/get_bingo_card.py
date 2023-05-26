
import random

unique_numbers = []

def get_one_line():
    my_str = ''
    for i in range(5):
        rnd = random.randint(1, 75)
        my_str += str(rnd).ljust(3)
    print(my_str)

def get_one_line_zero():
    my_str = ''
    my_list = []
    for i in range(5):
        rnd = random.randint(1, 75)
        my_list.append(rnd)
        # print(len(my_list))
        if len(my_list) == 3:
            my_str += '0'.ljust(3)
        else:
            my_str += str(rnd).ljust(3)
    print(my_str)

def get_bingo_card():
    for i in range(2):
        get_one_line()

get_bingo_card()
get_one_line_zero()
get_bingo_card()