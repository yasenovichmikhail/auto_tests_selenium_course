def from_fahrenheit_to_celsius(x):
    return (((x - 32) * 5) / 9)
    
x = float(input())
print(from_fahrenheit_to_celsius(x))