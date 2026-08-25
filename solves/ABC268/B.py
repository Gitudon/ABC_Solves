S = input()
T = input()

if len(S) <= len(T):
    a = len(S)
    b = T[:a]
    if S == b:
        print("Yes")
    else:
        print("No")
else:
    print("No")
