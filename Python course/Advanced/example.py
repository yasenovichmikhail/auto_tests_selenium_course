def get_req(num):
    if num <= 1:
        return
    else:
        num = num // 2
        print(num)
    get_req(num)


num = 101

get_req(num)