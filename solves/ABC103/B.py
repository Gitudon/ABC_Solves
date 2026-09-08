S = input()
T = input()

ans = "No"
for i in range(len(S)):
    S = S[-1] + S[:-1]
    if S == T:
        ans = "Yes"

print(ans)
