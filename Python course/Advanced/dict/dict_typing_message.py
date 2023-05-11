def get_typing_combination(text, numbers):
    my_list = list(text.upper())
    print(my_list)
    for i in my_list:
        # print(i)
        for key, value in numbers.items():
            # print(value)
                if i in value:
                    # print(key)
                    for j in range(len(value)):
                        if i != value[j]:
                            print(key)

numbers = {1: '.,?!:', 2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL',
 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ', 0: ' '}

text = 'Hello, World!'

get_typing_combination(text, numbers)