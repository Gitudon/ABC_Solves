N, Q = map(int, input().split())
A = list(map(int, input().split()))


def solve():
    maxv = 1_000_009
    accum_sum = [0] * (maxv + 1)
    accum_cnt = [0] * (maxv + 1)

    for i in range(N):
        accum_sum[A[i]] += A[i]
        accum_cnt[A[i]] += 1

    for i in range(1, maxv + 1):
        accum_sum[i] += accum_sum[i - 1]
        accum_cnt[i] += accum_cnt[i - 1]

    results = []
    for _ in range(Q):
        B = int(input())
        ans = 1 + accum_sum[B - 1] + (N - accum_cnt[B - 1]) * (B - 1)
        if accum_cnt[B - 1] == N:
            results.append("-1")
        else:
            results.append(str(ans))
    return results


results = solve()
for result in results:
    print(result)
