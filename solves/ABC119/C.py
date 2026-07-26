n, a, b, c = map(int, input().split())
l = [0] * n
for i in range(n):
    l[i] = int(input())


def solve(a2, b2, c2, l2):
    if len(l2) == 0:
        if a2 == 0 or b2 == 0 or c2 == 0:
            return 1000000000
        return abs(a - a2) + abs(b - b2) + abs(c - c2)
    return min(
        solve(a2, b2, c2, l2[1:]),
        solve(a2 + l2[0], b2, c2, l2[1:]) + 10,
        solve(a2, b2 + l2[0], c2, l2[1:]) + 10,
        solve(a2, b2, c2 + l2[0], l2[1:]) + 10,
    )


print(solve(0, 0, 0, l) - 30)
