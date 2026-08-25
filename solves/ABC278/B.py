H, M = map(int, input().split())


def dudge(H, M):
    A = H // 10
    B = H % 10
    C = M // 10
    D = M % 10
    if 0 <= A * 10 + C < 24 and 0 <= B * 10 + D < 60:
        return 1
    else:
        return 0


ans = []
for i in range(H, 24):
    if i == H:
        for j in range(M, 60):
            if dudge(i, j) == 1:
                ans.append([i, j])
    else:
        for j in range(60):
            if dudge(i, j) == 1:
                ans.append([i, j])
for i in range(H):
    for j in range(60):
        if dudge(i, j) == 1:
            ans.append([i, j])
print(ans[0][0], ans[0][1])
