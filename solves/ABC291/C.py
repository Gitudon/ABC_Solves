N = int(input())
S = input()

move = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
visited = set()
x, y = 0, 0
visited.add((x, y))
ans = "No"
for s in S:
    dx, dy = move[s]
    x += dx
    y += dy
    if (x, y) in visited:
        ans = "Yes"
    visited.add((x, y))
print(ans)
