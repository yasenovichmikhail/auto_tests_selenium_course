result = {}
dict_operations = {'W':'write', 'R':'read', 'X':'execute'}

for _ in range(int(input())):
    x = input().split()
    result[x[0]] = [dict_operations[i] for i in x[1:]]
    
for _ in range(int(input())):
    x = input().split()
    if x[0] in result[x[1]]:
        print("OK")
    else:
        print("Access denied")