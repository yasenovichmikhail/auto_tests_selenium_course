def read_and_write():
    with open('C:/input.txt', encoding='utf-8') as input:
        lst = [i.strip() for i in input]

    with open('C:/output.txt', 'w', encoding='utf-8') as output:
        for index, item in enumerate(lst, 1):
            print(f'{index}) {item}', sep='\n', file=output)

read_and_write()