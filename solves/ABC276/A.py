S = input()

ans = -1
a = len(S)
for i in range(a):
    if S[i] == "a":
        ans = i + 1
print(ans)
