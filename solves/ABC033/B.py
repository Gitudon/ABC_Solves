N = int(input())

S = [0] * N
P = [0] * N

for i in range(N):
    S[i], P[i] = map(str, input().split())
    P[i] = int(P[i])

population = sum(P)
kahansu = population // 2 + 1
ans = "atcoder"

for i in range(N):
    if P[i] >= kahansu:
        ans = S[i]

print(ans)
