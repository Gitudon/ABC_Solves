x1, y1, x2, y2 = map(int, input().split())

one = []
two = []
moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

for move in moves:
    one.append((x1 + move[0], y1 + move[1]))
    two.append((x2 + move[0], y2 + move[1]))

ans = "No"
for o in one:
    if o in two:
        ans = "Yes"
print(ans)
