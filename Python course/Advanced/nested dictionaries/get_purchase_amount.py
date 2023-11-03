result = {}

for _ in range(int(input())):
    name, product, count = input().split()
    result.setdefault(name, {})
    result[name][product] = result[name].get(product, 0) + int(count)
    
for key, value in sorted(result.items()):
    print(f"{key}:")
    for i in sorted(value):
        print(i, value[i])