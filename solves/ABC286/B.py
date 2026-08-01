N = int(input())
S = input()
ans = ""
for i in range(N - 1):
    if S[i] + S[i + 1] == "na":
        ans += "ny"
    else:
        ans += S[i]
ans += S[-1]
print(ans)
