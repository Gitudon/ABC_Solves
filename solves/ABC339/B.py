H, W, N = map(int, input().split())
grid = [["."] * W for _ in range(H)]
now = [0, 0]
toward = 0
for i in range(N):
    if grid[now[0]][now[1]] == ".":
        grid[now[0]][now[1]] = "#"
        if toward == 0:
            now[1] += 1
            if now[1] == W:
                now[1] = 0
        elif toward == 1:
            now[0] += 1
            if now[0] == H:
                now[0] = 0
        elif toward == 2:
            now[1] -= 1
            if now[1] == -1:
                now[1] = W - 1
        elif toward == 3:
            now[0] -= 1
            if now[0] == -1:
                now[0] = H - 1
        toward = (toward + 1) % 4
    else:
        grid[now[0]][now[1]] = "."
        if toward == 0:
            now[1] -= 1
            if now[1] == -1:
                now[1] = W - 1
        elif toward == 1:
            now[0] -= 1
            if now[0] == -1:
                now[0] = H - 1
        elif toward == 2:
            now[1] += 1
            if now[1] == W:
                now[1] = 0
        elif toward == 3:
            now[0] += 1
            if now[0] == H:
                now[0] = 0
        toward = (toward - 1) % 4
for i in range(H):
    print("".join(grid[i]))
