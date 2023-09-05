with open('C:/population.txt', encoding='utf-8') as population:
    lst_population = [i.strip().split('\t') for i in population.readlines()]
    # print(lst_population)
    for j in range(len(lst_population)):
        if lst_population[j][0][0] == 'G' and int(lst_population[j][1]) > 500_000:
            print(lst_population[j][0])