N, D = map(int, input().split())
S = [0] * N
for i in range(N):
    S[i] = input()
ans = []
tmp = 0
for j in range(D):
    for i in range(N):
        if S[i][j] == "x":
            ans.append(tmp)
            tmp = 0
            break
        elif i == N - 1:
            tmp += 1
    if j == D - 1:
        ans.append(tmp)
print(max(ans))
