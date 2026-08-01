N = int(input())
S = [0] * 51
for i in range(N):
    s = input()
    S[len(s)] = s
ans = ""
for i in range(51):
    if S[i] != 0:
        ans += S[i]
print(ans)
