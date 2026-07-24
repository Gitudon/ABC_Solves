N, K = map(int, input().split())

ans = [
    N,
    abs(N - K * (N // K)),
    abs(N - K * (N // K + 1)),
]

print(min(ans))
