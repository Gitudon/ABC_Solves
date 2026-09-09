N, X = map(int, input().split())
A = list(map(int, input().split()))

known = [0] * (N + 1)

while True:
    if known[X] == 1:
        break
    known[X] = 1
    X = A[X - 1]

ans = 0
for i in range(N):
    if known[i + 1] == 1:
        ans += 1
print(ans)
