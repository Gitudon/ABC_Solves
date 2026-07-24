N, Q = map(int, input().split())
A = list(map(int, input().split()))

B = A + A
for i in range(2 * N - 1, 0, -1):
    B[i - 1] += B[i]

rui_c = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = query[1]
        rui_c = (rui_c + c) % N
    else:
        l, r = query[1] - 1, query[2]
        print(B[l + rui_c] - B[r + rui_c])
