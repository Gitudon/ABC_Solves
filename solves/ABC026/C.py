N = int(input())
buka = [[] * N for _ in range(N)]
for i in range(N - 1):
    B = int(input())
    buka[B - 1].append(i + 1)


def dfs(v):
    if not buka[v]:
        return 1
    salaries = []
    for i in buka[v]:
        salaries.append(dfs(i))
    return min(salaries) + max(salaries) + 1


print(dfs(0))
