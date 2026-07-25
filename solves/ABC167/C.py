N, M, X = map(int, input().split())

C_A = [list(map(int, input().split())) for _ in range(N)]

C = [C_A[i][0] for i in range(N)]
A = [C_A[i][1:] for i in range(N)]

ans = []


def solve(count, skill, cost):
    if count == N:
        if all(s >= X for s in skill):
            ans.append(cost)
        return
    solve(count + 1, skill, cost)
    solve(count + 1, [skill[i] + A[count][i] for i in range(M)], cost + C[count])


solve(0, [0] * M, 0)

if ans == []:
    print(-1)
else:
    print(min(ans))
