

def the_product_of_numbers():
    s = [int(input()) for _ in range(int(input()))]
    result = int(input())
    Flag = False
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] * s[j] == result and i != j:
                Flag = True
                break
    if Flag == True:
        return True
    
def result():
    if the_product_of_numbers() == True:
        print('ДА')
    else:
        print('НЕТ')

result()
