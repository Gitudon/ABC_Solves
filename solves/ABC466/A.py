N = int(input())
X = list(map(int, input().split()))
ans = "Yes"
for i in range(N):
    if X[i] >= 0:
        ans = "No"
print(ans)
