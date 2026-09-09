N, M = map(int, input().split())
houses = [False] * N
for i in range(M):
    A, B = map(str, input().split())
    A = int(A)
    if houses[A - 1]:
        print("No")
    else:
        if B == "M":
            print("Yes")
            houses[A - 1] = True
        else:
            print("No")
