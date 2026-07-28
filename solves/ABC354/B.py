N = int(input())
zisyo = {}
for _ in range(N):
    S, C = input().split()
    zisyo[S] = int(C)
zisyo = sorted(zisyo.items(), key=lambda x: x[0])
T = 0
for i in range(N):
    T += zisyo[i][1]
bango = T % N
for i in range(N):
    if i == bango:
        print(zisyo[i][0])
