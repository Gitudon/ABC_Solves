K = int(input())
A, B = map(str, input().split())


def henkan(n):
    res = 0
    for i in range(len(n)):
        res += int(n[-i - 1]) * (K**i)
    return res


print(henkan(A) * henkan(B))
