N = int(input())
S = []
for i in range(N):
    S.append(input())
ans = 0
for i in range(N):
    if S[i] == "Takahashi":
        ans += 1
print(ans)
