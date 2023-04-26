a = '1930'
b = '2465748'
set_a = set(a)
set_b = set(b)
list = []

for i in set_a:
    if i not in list:
        list.append(i)
for j in set_b:
    if j not in list:
        list.append(j)

if len(list) == 10:
    print('YES')
elif len(list) != 10:
    print('NO')
else:
    print('Something went wrong')
