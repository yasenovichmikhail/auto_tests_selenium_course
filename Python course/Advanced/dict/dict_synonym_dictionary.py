
def get_synonym_dictionary(n):
    result = {}
    for i in range(n):
        list_syn = input().split(' ')
        for j in range(len(list_syn) - 1):
            result[list_syn[j]] = result.get(list_syn[j][0], list_syn[1])
#        print(list_syn)
#    print(result)
    word = input()
#    print(word)
    for key, value in result.items():
        if key == word:
            print(value)
        elif value == word:
            print(key)
n = int(input())

get_synonym_dictionary(n)