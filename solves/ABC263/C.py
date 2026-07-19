N, M = map(int, input().split())


def dfs(li):
    if len(li) == N:
        print(*li)
        return
    for i in range(li[-1] + 1, M + 1):
        dfs(li + [i])


for i in range(1, M + 1):
    dfs([i])
