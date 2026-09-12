S = input()
T = input()
ans = 0
if len(S) > len(T):
    T += "0" * (len(S) - len(T))
elif len(S) < len(T):
    S += "0" * (len(T) - len(S))
for i in range(len(S)):
    if S[i] != T[i]:
        ans = i + 1
        break
print(ans)
