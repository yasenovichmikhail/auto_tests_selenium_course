def get_single_number(num):
    my_dict = {}
    for i in num:
        my_dict[i] = my_dict.get(i, 0) + 1
    for key, value in my_dict.items():
        if value == 1:
            return key


nums = [4, 1, 2, 1, 2]

print(get_single_number(nums))