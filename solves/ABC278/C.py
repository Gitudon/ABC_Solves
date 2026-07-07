N, Q = map(int, input().split())

follow = {}

for i in range(Q):
    T, A, B = map(int, input().split())
    match T:
        case 1:
            if A not in follow:
                follow[A] = set()
            follow[A].add(B)
        case 2:
            if A not in follow:
                follow[A] = set()
            follow[A].discard(B)
        case 3:
            if A not in follow or B not in follow:
                print("No")
                continue
            if B in follow[A]:
                if A in follow[B]:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
