S = input()
T = input()

ans = 0

for i in range(len(S)):
    if S[i] != T[i]:
        ans = i + 1
        break

if ans == 0:
    print(len(T))
else:
    print(ans)
