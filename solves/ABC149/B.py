A, B, K = map(int, input().split())

if A >= K:
    print(A - K, B)
else:
    K -= A
    if B >= K:
        print(0, B - K)
    else:
        print(0, 0)
