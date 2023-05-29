
import random

unique_numbers = []

def get_one_line():
    my_str = ''
    line = []
    while len(line) != 5:
        rnd = random.randint(1, 75)
        if rnd not in unique_numbers:
            my_str += str(rnd).ljust(3)
            unique_numbers.append(rnd)
            line.append(rnd)
        else:
            continue
    print(my_str)

def get_one_line_zero():
    my_str = ''
    my_list = []
    line = []
    while len(line) != 5:
        rnd = random.randint(1, 75)
        # print(len(my_list))
        if rnd not in unique_numbers:
            unique_numbers.append(rnd)
            line.append(rnd)
            my_list.append(rnd)
            if len(my_list) == 3:
                my_str += '0'.ljust(3)
            else:
                my_str += str(rnd).ljust(3)
        else:
            continue
    print(my_str)

def get_bingo_card():
    for i in range(2):
        get_one_line()

get_bingo_card()
get_one_line_zero()
get_bingo_card()