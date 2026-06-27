N, M, Q = map(int, input().split())

full_auth = [0] * N
auth = [{} for _ in range(N)]


for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if query[2] not in auth[query[1] - 1]:
            auth[query[1] - 1][query[2]] = 1
    elif query[0] == 2:
        full_auth[query[1] - 1] += True
    elif query[0] == 3:
        if full_auth[query[1] - 1]:
            print("Yes")
        else:
            if query[2] in auth[query[1] - 1]:
                print("Yes")
            else:
                print("No")
