
def get_dictionary():
    s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
    x = s.split(' ')
    my_dict = {}
    for i in x:
        tmp = i.split(':')
        my_dict[int(tmp[0])] = my_dict.get(tmp[0], tmp[1])
        # print(tmp)
    print(my_dict)

get_dictionary()