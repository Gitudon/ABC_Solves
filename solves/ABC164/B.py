A, B, C, D = map(int, input().split())

round = 0
while A > 0 and C > 0:
    if round % 2 == 0:
        C -= B
    else:
        A -= D
    round += 1
if A <= 0:
    print("No")
else:
    print("Yes")
