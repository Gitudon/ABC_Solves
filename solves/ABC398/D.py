N, R, C = map(int, input().split())
S = input()

smoke_positions = set([(0, 0)])
directions = {"N": (1, 0), "W": (0, 1), "S": (-1, 0), "E": (0, -1)}
ans = ""
hito_ichi = (R, C)
takibi_ichi = (0, 0)

for t in range(N):
    dx, dy = directions[S[t]]
    hito_ichi = (hito_ichi[0] + dx, hito_ichi[1] + dy)
    takibi_ichi = (takibi_ichi[0] + dx, takibi_ichi[1] + dy)
    smoke_positions.add(takibi_ichi)
    if hito_ichi in smoke_positions:
        ans += "1"
    else:
        ans += "0"

print(ans)
