x, y, z = list(map(int, input().split()))

pencil_price = 3
pen_price = pencil_price + 2
tip_pen = pen_price + 7

total_sum = (x * pencil_price) + (y * pen_price) + (z * tip_pen)


print(total_sum)