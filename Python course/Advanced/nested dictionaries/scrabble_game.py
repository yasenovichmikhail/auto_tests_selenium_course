my_dict = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

s = input()

result = [ key for letter in s for key, value in my_dict.items() if letter in value]

print(sum(result))