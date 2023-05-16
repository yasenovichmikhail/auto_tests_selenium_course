
def get_the_most_famous_word(s):
    text = s.split(' ')
    result = {}
    tmp = 0
    my_list = []
    for i in text:
        result[i] = result.get(i, 0) + 1
    for key, value in result.items():
        if value > tmp:
            tmp = value
    for key1, value1 in result.items():
        if value1 == tmp:
            my_list.append(key1)
    print(min(my_list))

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

get_the_most_famous_word(s)