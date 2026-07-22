N, M = map(int, input().split())
H = list(map(int, input().split()))
tenbodai = [0] * (N)

for i in range(M):
    a, b = map(int, input().split())
    if tenbodai[a - 1] < H[b - 1]:
        tenbodai[a - 1] = H[b - 1]
    if tenbodai[b - 1] < H[a - 1]:
        tenbodai[b - 1] = H[a - 1]

ans = 0
for i in range(N):
    if tenbodai[i] < H[i]:
        ans += 1
print(ans)
