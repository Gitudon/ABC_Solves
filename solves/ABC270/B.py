X, Y, Z = map(int, input().split())

if X > 0:
    if Y > X:
        print(X)
    elif Y < X and Y < 0:
        print(X)
    elif Y < X and Y > 0:
        if Z > Y:
            print(-1)
        else:
            if Z > 0:
                print(X)
            else:
                print(2 * abs(Z) + X)
if X < 0:
    if X > Y:
        print(abs(X))
    elif Y > X and Y > 0:
        print(abs(X))
    elif Y > X and Y < 0:
        if Z < Y:
            print(-1)
        else:
            if Z < 0:
                print(abs(X))
            else:
                print(2 * Z + abs(X))
