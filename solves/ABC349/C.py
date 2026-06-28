S = input()
T = input()

ans = "No"
if T[-1] == "X":
    flag1 = False
    for i in range(len(S)):
        if not flag1:
            if S[i].upper() == T[0]:
                flag1 = True
        else:
            if S[i].upper() == T[1]:
                ans = "Yes"
                break

flag1 = False
flag2 = False
for i in range(len(S)):
    if not flag1:
        if S[i].upper() == T[0]:
            flag1 = True
    else:
        if not flag2:
            if S[i].upper() == T[1]:
                flag2 = True
        else:
            if S[i].upper() == T[2]:
                ans = "Yes"
                break

print(ans)
