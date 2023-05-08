def get_mixed_students(num1, num2):
    set_math = set()
    set_inform = set()
    for i in range(num1):
        sur_name = input()
        if sur_name in set_math:
            set_inform.add(sur_name)
        set_math.add(sur_name)
    for i in range(num2):
        sur_name = input()
        if sur_name in set_inform:
            set_math.add(sur_name)
        set_inform.add(sur_name)
    result = len(set_math.symmetric_difference(set_inform))
    if result > 0:
        print(result)
    else:
        print('NO')
    
num1 = int(input())
num2 = int(input())

get_mixed_students(num1, num2)