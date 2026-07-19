N = int(input())

X = 10000
Y = 10000

for _ in range(N):
    A, B, S = map(str, input().split())
    A = int(A)
    B = int(B)
    if S == "take":
        X += B - A
    Y += B - A

print(Y - X)
