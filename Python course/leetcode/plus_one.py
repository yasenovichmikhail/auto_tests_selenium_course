def plus_one(nums):
    lst = []
    st = map(str, nums)
    str_res = ''.join(st)
    integer_result = int(str_res) + 1
    while integer_result > 0:
        num = integer_result % 10
        integer_result = integer_result // 10
        lst.append(num)
    lst = lst[::-1]
    return lst


digits = [1, 2, 9]

print(plus_one(digits))
