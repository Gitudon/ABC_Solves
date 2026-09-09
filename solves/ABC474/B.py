N = int(input())
P = list(map(int, input().split()))

ans = "Yes"
for i in range(N):
    now = i // 10
    if not (now * 10 <= P[i] - 1 < (now + 1) * 10):
        ans = "No"
print(ans)
