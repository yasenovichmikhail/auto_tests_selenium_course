import string as s
import random


letters = s.ascii_letters

def generate_random_characters(num_char):
    result = ''
    for i in range(num_char):
        x = random.choice(letters)
        result += x
    return(result)

print(generate_random_characters(15))