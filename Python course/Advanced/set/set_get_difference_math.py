def get_learn_math(num1, num2):
    set_math = set()
    set_phys = set()
    for i in range(num1):
        sur_name = input()
        set_math.add(sur_name)
    for i in range(num2):
        sur_name = input()
        set_phys.add(sur_name)
    result = len(set_math.difference(set_phys))
    print(result)
    
num1 = int(input())
num2 = int(input())

get_learn_math(num1, num2)