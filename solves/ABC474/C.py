N, Q = map(int, input().split())
P = list(map(int, input().split()))

junban = P + [0] * Q
basho = [0] * N
for i in range(N):
    basho[P[i] - 1] = i

for q in range(Q):
    a = int(input()) - 1
    junban[basho[a]] = 0
    junban[N + q] = a + 1
    basho[a] = N + q

ans = []
for j in junban:
    if j != 0:
        ans.append(j)

print(*ans)
