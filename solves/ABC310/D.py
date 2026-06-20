def dfs(hate, teams, now):
    if now == N:
        return len(teams) == T
    ans = 0
    for i, team in enumerate(teams):
        if not (team & hate[now]):
            teams[i] ^= 1 << now
            ans += dfs(hate, teams, now + 1)
            teams[i] ^= 1 << now
    if len(teams) < T:
        teams.append(1 << now)
        ans += dfs(hate, teams, now + 1)
        teams.pop()
    return ans


N, T, M = map(int, input().split())
hate = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    hate[b - 1] |= 1 << (a - 1)
teams = []
result = dfs(hate, teams, 0)
print(result)
