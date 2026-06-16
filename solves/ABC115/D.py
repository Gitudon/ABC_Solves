N, X = map(int, input().split())


def hamburger(n, x):
    if n == 0:
        return 1
    length = (1 << (n + 1)) - 3
    num = (1 << n) - 1
    if x == 1:
        return 0
    elif x <= length + 1:
        return hamburger(n - 1, x - 1)
    elif x == length + 2:
        return num + 1
    elif x <= (length + 1) * 2:
        return num + 1 + hamburger(n - 1, x - length - 2)
    else:
        return num * 2 + 1


print(hamburger(N, X))
