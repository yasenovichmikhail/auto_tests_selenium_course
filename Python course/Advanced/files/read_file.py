name_file = input()

def read_file(name_file):
    file = open(name_file, 'r', encoding='utf-8')
    view_file = file.read()
    print(view_file)

read_file(name_file)