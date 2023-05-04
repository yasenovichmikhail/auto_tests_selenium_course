
#Example1
items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45,
 '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]

result = {i if type(i) == int else int(i) for i in items}

print(*sorted(result))

#Example2
words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry',
 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']

words1 = {i[0].lower() for i in words}
my_set = set(words1)

print(*sorted(my_set))