S = input()
T = input()

ans = []
i = 0
j = 0
while i < (len(S)):
    if S[i] == T[j]:
        ans.append(j + 1)
        i += 1
    j += 1
print(*ans)
