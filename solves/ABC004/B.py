N = 4
c = [0] * N
for i in range(N):
    c[i] = input().split()

for i in range(N):
    ans = ""
    for j in range(N):
        ans += c[N - 1 - i][N - 1 - j] + " "
    ans = ans[:-1]
    print(ans)
