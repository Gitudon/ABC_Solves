X = int(input())
kuku = [[0] * 9 for i in range(9)]
for i in range(9):
    for j in range(9):
        kuku[i][j] = (i + 1) * (j + 1)
ans = 0
for i in range(9):
    for j in range(9):
        if kuku[i][j] != X:
            ans += kuku[i][j]
print(ans)
