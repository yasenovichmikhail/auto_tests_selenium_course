point = [(1, 2), (15, 1), (5, -1), (10, 4)]

points_sorted = sorted(point, key=lambda x: x[0]+ x[1])

print(points_sorted)