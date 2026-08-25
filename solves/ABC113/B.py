N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans = 0
min_diff = 10**9

for i in range(N):
    diff = T - H[i] * 0.006
    if abs(diff - A) < min_diff:
        min_diff = abs(diff - A)
        ans = i + 1
print(ans)
