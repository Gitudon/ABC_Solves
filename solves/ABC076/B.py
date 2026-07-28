N = int(input())
K = int(input())
ans = []


def solve(n, k):
    if n == 0:
        ans.append(k)
        return
    solve(n - 1, k * 2)
    solve(n - 1, k + K)


solve(N, 1)
print(min(ans))
