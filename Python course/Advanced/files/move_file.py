import os

source = "c:/Users/zeta/auto_tests_selenium_course/Python course/Advanced/files/test.txt"
destination = "C:\\Users\\zeta\\desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source +" was moved")
except FileNotFoundError:
    print(source + " was not found")
