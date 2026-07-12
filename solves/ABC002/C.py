x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())

zahyo = [(x_a, y_a), (x_b, y_b), (x_c, y_c)]
zahyo.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)

x = zahyo[0][0]
y = zahyo[0][1]
for i in range(3):
    zahyo[i] = (zahyo[i][0] - x, zahyo[i][1] - y)

print(abs(zahyo[1][0] * zahyo[2][1] - zahyo[1][1] * zahyo[2][0]) / 2)
