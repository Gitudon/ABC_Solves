A, B = map(int, input().split())


def S(n):
    N = str(n)
    return int(N[0]) + int(N[1]) + int(N[2])


if S(A) >= S(B):
    print(S(A))
else:
    print(S(B))
