N = int(input())
S = input()

ans = ""
ans += S[0]
for i in range(1, N):
    if S[i] != S[i - 1]:
        ans += S[i]
print(len(ans))
