H, W = map(int, input().split())
G = [input() for _ in range(H)]

visited = [[False] * W for _ in range(H)]

current = (0, 0)
while True:
    i = current[0]
    j = current[1]
    if visited[current[0]][current[1]]:
        print(-1)
        break
    visited[i][j] = True
    if G[i][j] == "U":
        if i == 0:
            print(current[0] + 1, current[1] + 1)
            break
        else:
            current = (i - 1, j)
    elif G[i][j] == "D":
        if i == H - 1:
            print(current[0] + 1, current[1] + 1)
            break
        else:
            current = (i + 1, j)
    elif G[i][j] == "L":
        if j == 0:
            print(current[0] + 1, current[1] + 1)
            break
        else:
            current = (i, j - 1)
    elif G[i][j] == "R":
        if j == W - 1:
            print(current[0] + 1, current[1] + 1)
            break
        else:
            current = (i, j + 1)
