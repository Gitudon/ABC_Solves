N = int(input())


def solve(N):
    if N == 0:
        return ["#"]
    else:
        prev = solve(N - 1)
        l = len(prev)
        ans = [["." for _ in range(3 * l)] for _ in range(3 * l)]
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                else:
                    for k in range(l):
                        for m in range(l):
                            ans[i * l + k][j * l + m] = prev[k][m]
        return ans


ans = solve(N)
for a in ans:
    print("".join(a))
