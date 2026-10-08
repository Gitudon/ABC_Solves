N, X, Y, Z = map(int, input().split())
up = True
if X > Y:
    up = False
if up:
    if X < Z < Y:
        print("Yes")
    else:
        print("No")
else:
    if X > Z > Y:
        print("Yes")
    else:
        print("No")
