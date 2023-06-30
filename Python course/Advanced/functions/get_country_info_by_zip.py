countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

def get_country_info(countries, capitals, population):
    result = list(zip(capitals, countries, population))
    for i in result:
        print(f'{i[0]} is the capital of {i[1]}, population equal {i[2]} people.')

get_country_info(countries, capitals, population)