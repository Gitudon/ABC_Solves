N, Q = map(int, input().split())
A = [i + 1 for i in range(N)]


def change_index(index, now):
    return (index + now) % N


now = 0
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        p = int(query[1]) - 1
        x = int(query[2])
        A[change_index(p, now)] = x
    elif query[0] == "2":
        p = int(query[1]) - 1
        print(A[(change_index(p, now))])
    elif query[0] == "3":
        k = int(query[1])
        now += k
