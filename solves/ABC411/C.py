N, Q = map(int, input().split())
A = list(map(int, input().split()))

masu = [False] * N
kukan = 0

for i in range(Q):
    if not masu[A[i] - 1]:
        masu[A[i] - 1] = True
        if N == 1:
            print(1)
            continue
        if A[i] == 1:
            if not masu[A[i]]:
                kukan += 1
        elif A[i] == N:
            if not masu[A[i] - 2]:
                kukan += 1
        else:
            if masu[A[i]]:
                if masu[A[i] - 2]:
                    kukan -= 1
            else:
                if not masu[A[i] - 2]:
                    kukan += 1
    else:
        masu[A[i] - 1] = False
        if N == 1:
            print(0)
            continue
        if A[i] == 1:
            if not masu[A[i]]:
                kukan -= 1
        elif A[i] == N:
            if not masu[A[i] - 2]:
                kukan -= 1
        else:
            if masu[A[i]]:
                if masu[A[i] - 2]:
                    kukan += 1
            else:
                if not masu[A[i] - 2]:
                    kukan -= 1
    print(kukan)
