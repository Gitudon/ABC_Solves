N, S, T = map(int, input().split())
W = int(input())
A = []
for i in range(N - 1):
    A.append(int(input()))
ans = 0
if S <= W <= T:
    ans += 1
for i in range(N - 1):
    W += A[i]
    if S <= W <= T:
        ans += 1
print(ans)
