S = input()

ans = "Yes"
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] not in ["R", "U", "D"]:
            ans = "No"
    else:
        if S[i] not in ["L", "U", "D"]:
            ans = "No"

print(ans)
