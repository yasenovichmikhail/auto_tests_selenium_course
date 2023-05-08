def get_only_one_subject(num1, num2):
    set_math = set()
    set_inform = set()
    for i in range(num1):
        sur_name = input()
        set_math.add(sur_name)
    for i in range(num2):
        sur_name = input()
        set_inform.add(sur_name)
    result = len(set_math.symmetric_difference(set_inform))
    if result > 0:
        print(result)
    else:
        print('NO')
    
num1 = int(input())
num2 = int(input())

get_only_one_subject(num1, num2)