points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

def sorted_points(point):
    som = sorted(point, key=lambda x: x[0]**2 + x[1]**2)
    print(som)

sorted_points(points)

def squares(point):
    return point[0]**2 + point[1]**2

print(sorted(points, key=squares))