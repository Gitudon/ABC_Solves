N, A, B = map(int, input().split())

tairu = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            if j % 2 == 0:
                tairu[i][j] = "."
            else:
                tairu[i][j] = "#"
        else:
            if j % 2 == 0:
                tairu[i][j] = "#"
            else:
                tairu[i][j] = "."
for i in range(N):
    ans = ""
    for j in range(N):
        for k in range(B):
            ans += tairu[i][j]
    for j in range(A):
        print(ans)
