N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

see = [0] * (N + 1)
for i in range(1, N + 1):
    see[i] = P[i - 1]

zekken = [0] * (N + 1)
for i in range(1, N + 1):
    zekken[Q[i - 1]] = i

taio = [0] * (N + 1)
for i in range(1, N + 1):
    taio[zekken[i]] = i

ans = [0] * (N + 1)
for i in range(1, N + 1):
    hito1 = zekken[i]
    hito2 = see[hito1]
    ans[i] = taio[hito2]

print(*ans[1:])
