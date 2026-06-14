from numpy import cumsum
from bisect import bisect_left

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = int(input())
cumsum_ = cumsum(P)
for _ in range(Q):
    L, R = map(int, input().split())
    L_idx = bisect_left(X, L)
    R_idx = bisect_left(X, R + 1)
    if L_idx < R_idx:
        if L_idx == 0:
            print(cumsum_[R_idx - 1])
        else:
            print(cumsum_[R_idx - 1] - cumsum_[L_idx - 1])
    else:
        print(0)
