

def get_unique_extension(files):

    my_set = {files[i].lower() for i in range(len(files)) if files[i][-3:].lower() == 'png'}
    print(*sorted(my_set))

files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']

get_unique_extension(files)