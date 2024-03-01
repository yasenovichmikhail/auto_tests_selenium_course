weather = {'New York':"snowing", 'Boston':"sunny", 'Los Angeles':"sunny", 'Chicago':"cloudy" }

cities_in_F = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}
cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
cities = cities_in_F = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}
desc_cities = {key: "WARM" if value >= 40 else "COLD" for (key,value) in cities.items()}

def check_temp(value):
    if value >= 40:
        return "WARM"
    else:
        return "COLD"


desc_cities_func = {key: check_temp(value) for (key,value) in cities.items()}

print(desc_cities_func)
print(cities_in_C)
print(sunny_weather)
print(desc_cities)

