S, T, X = map(int, input().split())

if S < T:
    if S * 60 <= X * 60 + 30 < T * 60:
        print("Yes")
    else:
        print("No")
elif S > T and S > X:
    T += 24
    X += 24
    if S * 60 <= X * 60 + 30 < T * 60:
        print("Yes")
    else:
        print("No")
else:
    T += 24
    if S * 60 <= X * 60 + 30 < T * 60:
        print("Yes")
    else:
        print("No")
