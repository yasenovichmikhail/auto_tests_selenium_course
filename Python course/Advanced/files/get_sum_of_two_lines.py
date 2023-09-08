
def get_sum_of_two_line2():
    file = open('C:/nums.txt', encoding='utf-8')
    
    lst = [int(i) for i in file.read().split()]
    print(sum(lst))
    
    file.close()
    
get_sum_of_two_line2()