N = int(input())
grid = [["."] * N for _ in range(N)]
for i in range(N):
    j = N - 1 - i
    if i <= j:
        if i % 2 == 0:
            for k in range(i, j + 1):
                for l in range(i, j + 1):
                    grid[k][l] = "#"
        else:
            for k in range(i, j + 1):
                for l in range(i, j + 1):
                    grid[k][l] = "."

for i in range(N):
    print("".join(grid[i]))
