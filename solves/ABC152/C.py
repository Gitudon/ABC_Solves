N = int(input())
P = list(map(int, input().split()))

ans = 0
current_min = P[0]
for i in range(N):
    if P[i] <= current_min:
        ans += 1
    current_min = min(current_min, P[i])
print(ans)
