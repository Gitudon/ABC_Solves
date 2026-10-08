N = int(input())
P = list(map(int, input().split()))
saikyo = max(P)
if P[0] == saikyo:
    for i in range(1, N):
        if P[i] == saikyo:
            print(1)
            exit()
    print(0)
else:
    print(saikyo - P[0] + 1)
