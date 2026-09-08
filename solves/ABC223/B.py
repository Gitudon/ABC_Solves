S = input()
T = S
ans = []

for i in range(len(S)):
    ans.append(S)
    S = S[-1] + S[:-1]
for i in range(len(T)):
    ans.append(T)
    T = T[1:] + T[0]

ans = list(set(ans))
ans.sort()
print(ans[0])
print(ans[-1])
