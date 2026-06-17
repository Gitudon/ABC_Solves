N = int(input())
L = 1
R = N
while 1 < (R - L):
    m = (L + R) // 2
    print("? " + str(m))
    a = int(input())
    if a == 0:
        L = m
    else:
        R = m
print("! " + str(L))
