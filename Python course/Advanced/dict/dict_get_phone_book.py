
def get_phone_book(n):
    result = {}
    for i in range(n):
        text = input().lower()
        list_or = text.split(' ')
        for j in range(len(list_or)):
            result[list_or[0]] = result.get(list_or[0], list_or[1])
    print(result)
    m = int(input())
    
    def in_list(result, name):
        for val1 in result.values():
            if name in result.values():
                return True
            
    for j in range(m):
        name = input().lower()
        if in_list(result, name):
            for key, value in result.items():
                if value == name:
                    print(key)
        else:
            print('абонент не найден')
    
n = int(input())

get_phone_book(n)