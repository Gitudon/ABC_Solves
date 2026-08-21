N, S, D = map(int, input().split())
ans = "No"
for i in range(N):
    X, Y = map(int, input().split())
    if X < S and Y > D:
        ans = "Yes"
print(ans)
