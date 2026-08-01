N = int(input())

S = []
for i in range(N):
    s = input()
    S.append(s)

S = list(set(S))
ans = {}
for i in range(len(S)):
    for j in range(len(S)):
        if i != j:
            if S[i] + S[j] not in ans:
                ans[S[i] + S[j]] = 1
print(len(ans))
