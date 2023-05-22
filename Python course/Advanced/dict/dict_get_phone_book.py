
def get_phone_book(n):
    phone_book = {}
    for i in range(n):
        mobile, name = input().lower().split()
        phone_book.setdefault(name, []).append(mobile)
#    print(phone_book)
    m = int(input())
    
    def in_list(phone_book, name_srch):
        for val in phone_book.keys():
            if name_srch in phone_book.keys():
                return True
    
    for j in range(m):
        name_srch = input().lower()
        if in_list(phone_book, name_srch):
            for key, value in phone_book.items():
                if name_srch == key:
                    print(*value)
        else:
            print('абонент не найден')
    
n = int(input())

get_phone_book(n)