from collections import deque

Q = int(input())
A = deque()
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        c = int(query[1])
        x = int(query[2])
        A.append((x, c))
    elif query[0] == "2":
        k = int(query[1])
        arg = 0
        while k > 0 and A:
            x, c = A.popleft()
            if c <= k:
                k -= c
                arg += x * c
            else:
                A.appendleft((x, c - k))
                arg += x * k
                k = 0
        print(arg)
