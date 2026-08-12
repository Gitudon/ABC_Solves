hukuro = []
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        hukuro.append(query[1])
    elif query[0] == 2:
        hukuro = sorted(hukuro)
        print(hukuro.pop(0))
