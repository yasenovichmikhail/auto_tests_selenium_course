
def get_country_by_city(n):
    result = {}
    for i in range(n):
        city = []
        list_country = input().split(' ')
        city.append(list_country[1:])
        for j in range(len(list_country)):
            result[list_country[0]] = result.get(list_country[0], city)
#    print(result['Германия'])
#    print(result['Нидерланды'])
#    print(result)
    m = int(input())
    for k in range(m):
        name = input()
        for key, value in result.items():
#            print(key)
#            print(value)
            for b in range(len(value)):
                for t in range(len(value[b])):
                    if name == value[b][t]:
                        print(key)
            
n = int(input())

get_country_by_city(n)