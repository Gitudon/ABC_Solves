N, S = map(int, input().split())
T = list(map(int, input().split()))

kizyun = S + 0.5
ans = "Yes"
T = [0] + T + [S]
for i in range(N):
    if T[i + 1] - T[i] > kizyun:
        ans = "No"
print(ans)
