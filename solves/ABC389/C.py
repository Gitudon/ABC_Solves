from collections import deque

Q = int(input())
hebi = deque()
length = deque()
total = 0

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        if not hebi:
            hebi.append(0)
        else:
            hebi.append(hebi[-1] + length[-1])
        length.append(int(query[1]))
    elif query[0] == "2" and length:
        total += length.popleft()
        hebi.popleft()
    elif query[0] == "3":
        print(hebi[int(query[1]) - 1] - total)
