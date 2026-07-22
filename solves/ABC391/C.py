N, Q = map(int, input().split())
nest = [1] * (N + 1)
nest[0] = 0
bird = [0] * (N + 1)
for i in range(1, N + 1):
    bird[i] = i
arg = 0
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        P = int(query[1])
        H = int(query[2])
        nest[bird[P]] -= 1
        if nest[bird[P]] == 1:
            arg -= 1
        bird[P] = H
        nest[H] += 1
        if nest[H] == 2:
            arg += 1
    else:
        print(arg)
