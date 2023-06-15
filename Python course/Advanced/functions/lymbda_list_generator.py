# example1
tables = [lambda x = x: x*10 for x in range(1, 11)]
for table in tables:
    print(table())

# example2
max_number = lambda a, b: a if a > b else b
print(max_number(3, 5))