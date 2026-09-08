H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]
T = input()

houses = [[False] * W for _ in range(H)]
current = (X - 1, Y - 1)
ans = 0
for i in range(len(T)):
    if S[current[0]][current[1]] == "@":
        if houses[current[0]][current[1]] == False:
            houses[current[0]][current[1]] = True
            ans += 1
    if T[i] == "U" and S[current[0] - 1][current[1]] != "#":
        current = (current[0] - 1, current[1])
    elif T[i] == "D" and S[current[0] + 1][current[1]] != "#":
        current = (current[0] + 1, current[1])
    elif T[i] == "L" and S[current[0]][current[1] - 1] != "#":
        current = (current[0], current[1] - 1)
    elif T[i] == "R" and S[current[0]][current[1] + 1] != "#":
        current = (current[0], current[1] + 1)
if S[current[0]][current[1]] == "@":
    if houses[current[0]][current[1]] == False:
        houses[current[0]][current[1]] = True
        ans += 1
print(current[0] + 1, current[1] + 1, ans)
