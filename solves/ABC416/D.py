for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())))
    C, idx = 0, 0
    for v in A:
        while idx < N and B[idx] + v < M:
            idx += 1
        if idx >= N:
            break
        C += 1
        idx += 1
    print(sum(A) + sum(B) - M * C)
