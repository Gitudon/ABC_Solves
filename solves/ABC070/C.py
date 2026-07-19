N = int(input())
T = [0] * N
for i in range(N):
    T[i] = int(input())


def gcd(m, n):
    r = m % n
    if r == 0:
        return n
    return gcd(n, r)


def lcm(m, n):
    return m * n // gcd(m, n)


ans = T[0]
for i in range(1, N):
    ans = lcm(ans, T[i])
print(ans)
