N, K = map(int, input().split())
S = input()
ans = 0
zyotai = 0
for i in range(N):
    if S[i] == "O":
        zyotai += 1
    else:
        zyotai = 0
    if zyotai == K:
        ans += 1
        zyotai = 0
print(ans)
