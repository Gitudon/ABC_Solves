R = int(input())


def in_circle(i, j):
    return (2 * i + 1) ** 2 + (2 * j + 1) ** 2 <= 4 * (R**2)


cnt = 0
up = R - 1
res = up * 4 + 1
x = 1
while in_circle(x, 1):
    while not in_circle(x, up):
        up -= 1
    cnt += up
    x += 1
res += cnt * 4
print(res)
