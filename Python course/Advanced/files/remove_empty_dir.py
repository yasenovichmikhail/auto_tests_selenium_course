import os

path = "C:\\Users\\zeta\\auto_tests_selenium_course\\Python course\\Advanced\\files"

try:
    os.rmdir(path)
    print("The folder was deleted")
except FileNotFoundError:
    print("That folder was not found")