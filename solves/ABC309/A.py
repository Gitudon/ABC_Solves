A, B = map(int, input().split())
if B % 3 == 0:
    if B - A == 1:
        print("Yes")
    else:
        print("No")
elif B % 3 == 2:
    if B - A == 1:
        print("Yes")
    else:
        print("No")
else:
    print("No")
