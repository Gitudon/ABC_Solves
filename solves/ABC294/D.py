N, Q = map(int, input().split())
called1 = 0
called2 = 0
gone = [0] * N
for i in range(Q):
    e = list(map(int, input().split()))
    if e[0] == 1:
        called1 += 1
    elif e[0] == 2:
        gone[e[1] - 1] = 1
    else:
        while gone[called2] == 1:
            called2 += 1
        print(called2 + 1)
