N = int(input())

S = [0] * N
T = [0] * N
for i in range(N):
    S[i], T[i] = map(str, input().split())

ans = "No"
for i in range(N):
    for j in range(i + 1, N):
        if S[i] == S[j] and T[i] == T[j]:
            ans = "Yes"
print(ans)
