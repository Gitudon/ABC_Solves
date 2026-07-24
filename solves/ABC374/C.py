N = int(input())
K = list(map(int, input().split()))

ans = 10**10


def bit_zentansaku(n, A, B):
    global ans
    if n == N:
        ans = min(ans, max(A, B))
        return
    bit_zentansaku(n + 1, A + K[n], B)
    bit_zentansaku(n + 1, A, B + K[n])


bit_zentansaku(0, 0, 0)
print(ans)
