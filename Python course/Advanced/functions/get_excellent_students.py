n = int(input())
def get_excellent_students(n):
    all_students = []
    for i in range(n):
        classes = int(input())
        class_bool = []
        for j in range(classes):
            name = input()
            result = any(map(lambda x: x[-1] == '5', name))
            class_bool.append(result)
#            print(result)
        excellent = any(class_bool)
        all_students.append(excellent)
#        print(excellent)
    if all(all_students):
        print('YES')
    else:
        print('NO')
#    print(all_students)
        
get_excellent_students(n)