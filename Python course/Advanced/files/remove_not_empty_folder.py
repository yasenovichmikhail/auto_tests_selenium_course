import os
import shutil

path = "C:\\Users\\zeta\\auto_tests_selenium_course\\Python course\\Advanced\\files"

try:
    shutil.rmtree(path)
    print("The folder and files were deleted")
except FileNotFoundError:
    print("That folder was not found")