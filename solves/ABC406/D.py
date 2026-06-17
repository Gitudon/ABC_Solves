H, W, N = map(int, input().split())

X = [0] * N
Y = [0] * N

yoko = [0] * W
tate = [0] * H

yoko_exist = {i: set() for i in range(H)}
tate_exist = {i: set() for i in range(W)}

for i in range(N):
    X[i], Y[i] = map(int, input().split())
    tate[X[i] - 1] += 1
    yoko_exist[X[i] - 1].add(Y[i] - 1)
    yoko[Y[i] - 1] += 1
    tate_exist[Y[i] - 1].add(X[i] - 1)

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1] - 1
        print(f"{tate[x]}")
        for j in yoko_exist.get(x, []):
            yoko[j] -= 1
            tate_exist[j].discard(x)
        tate[x] = 0
        yoko_exist[x].clear()
    elif query[0] == 2:
        y = query[1] - 1
        print(f"{yoko[y]}")
        for j in tate_exist.get(y, []):
            tate[j] -= 1
            yoko_exist[j].discard(y)
        yoko[y] = 0
        tate_exist[y].clear()
