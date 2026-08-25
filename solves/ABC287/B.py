N, M = map(int, input().split())
S = [0] * N
T = [0] * M
for i in range(N):
    S[i] = input()
for i in range(M):
    T[i] = input()
ans = 0
for i in range(N):
    for j in range(M):
        if S[i][-3:] == T[j]:
            ans += 1
            break
print(ans)
