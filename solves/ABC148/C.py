A, B = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)


print(A * B // gcd(A, B))
