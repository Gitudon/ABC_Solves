L1, R1, L2, R2 = map(int, input().split())

if R1 <= L2:
    print(0)
elif R2 <= L1:
    print(0)
elif L1 == L2:
    if R1 == R2:
        print(R1 - L1)
    elif R1 < R2:
        print(R1 - L1)
    elif R1 > R2:
        print(R2 - L1)
elif L1 < L2:
    if R1 == R2:
        print(R1 - L2)
    elif R1 < R2:
        print(R1 - L2)
    elif R1 > R2:
        print(R2 - L2)
else:
    if R1 == R2:
        print(R1 - L1)
    elif R1 < R2:
        print(R1 - L1)
    elif R1 > R2:
        print(R2 - L1)
