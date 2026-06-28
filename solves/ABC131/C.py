from math import gcd

A, B, C, D = map(int, input().split())


def count(N, C, D):
    G = gcd(C, D)
    L = C * D // G
    return N - N // C + N // D - N // L


print(count(B, C, D) - count(A - 1, C, D))
