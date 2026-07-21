A = [[] for _ in range(9)]
for i in range(9):
    A[i] = list(map(int, input().split()))

mihon = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ans = "Yes"
for i in range(9):
    if sorted(A[i]) != mihon:
        ans = "No"
for i in range(9):
    buf = []
    for j in range(9):
        buf.append(A[j][i])
    if sorted(buf) != mihon:
        ans = "No"
for i in range(3):
    for j in range(3):
        buf = []
        for k in range(3):
            for l in range(3):
                buf.append(A[i * 3 + k][j * 3 + l])
        if sorted(buf) != mihon:
            ans = "No"
print(ans)
