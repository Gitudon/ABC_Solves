N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = 0
done = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if (i, j) in done:
            continue
        done.append((i, j))
        done.append((j, i))
        flag = True
        for k in range(M):
            if not (S[i][k] == "o" or S[j][k] == "o"):
                flag = False
                break
        if flag:
            ans += 1
print(ans)
