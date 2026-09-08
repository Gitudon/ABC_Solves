a, b = map(int, input().split())

towers = [0] * 1000

current = 0
for i in range(1, 1000):
    current += i
    towers[i] = current

ans = 0
for i in range(1, 1000):
    for j in range(i + 1, 1000):
        if towers[j] - towers[i] == (b - a):
            ans = towers[i] - a
print(ans)
