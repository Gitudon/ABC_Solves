N = int(input())
s = [0] * N
for i in range(N):
    s[i] = list(input())

for i in range(N):
    ans = ""
    for j in range(N):
        ans += s[N - j - 1][i]
    print(ans)
