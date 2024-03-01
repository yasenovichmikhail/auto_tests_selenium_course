import os

path = "C:\\Users\\zeta\\auto_tests_selenium_course\\Python course\\Advanced\\files\\test.txt"

try:
    os.remove(path)
    print("The file was deleted")
except FileNotFoundError:
    print("That file was not found")