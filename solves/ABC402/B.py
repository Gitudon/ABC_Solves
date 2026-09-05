Q = int(input())

machi = []

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        machi.append(query[1])
    elif query[0] == 2:
        print(machi.pop(0))
