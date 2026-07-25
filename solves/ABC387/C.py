L, R = map(int, input().split())
dictionary = {}


def solve(n, k):
    if n <= 0:
        return 0
    if (n, k) in dictionary:
        return dictionary[n, k]
    res = 0
    for i in range(10):
        res += solve((n - i) // 10, max(k, i))
    res += max(min(n, 9) - k, 0)
    dictionary[n, k] = res
    return res


ans = solve(R, 0) - solve(L - 1, 0)
print(ans)
