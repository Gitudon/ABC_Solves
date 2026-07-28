S = input()
T = input()

ans = "You can win"
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    elif S[i] == "@" and T[i] in ["@", "a", "t", "c", "o", "d", "e", "r"]:
        continue
    elif S[i] in ["@", "a", "t", "c", "o", "d", "e", "r"] and T[i] == "@":
        continue
    else:
        ans = "You will lose"
print(ans)
