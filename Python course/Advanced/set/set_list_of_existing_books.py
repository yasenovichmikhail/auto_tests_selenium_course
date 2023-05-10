def is_there_book(num, num1):
    set_books = set()
    recommend_books = set()
    for i in range(num):
        book_names = input()
        set_books.add(book_names)
    for i in range(num1):
        book_names = input()
        recommend_books.add(book_names)
#        print(recommend_books)
        if len(set_books.union(recommend_books)) > len(set_books):
            print('NO')
        else:
            print('YES')
        recommend_books.clear()
    
num = int(input())
num1 = int(input())

is_there_book(num, num1)