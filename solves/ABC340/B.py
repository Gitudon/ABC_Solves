Q = int(input())
A = []
for _ in range(Q):
    q1, q2 = map(int, input().split())
    if q1 == 1:
        A.append(q2)
    else:
        print(A[-q2])
