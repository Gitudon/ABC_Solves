N, Q = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)
for _ in range(Q):
    x = int(input())
    left, right = 0, N
    while left < right:
        mid = (left + right) // 2
        if A[mid] < x:
            left = mid + 1
        else:
            right = mid
    print(N - left)
