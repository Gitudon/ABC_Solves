A, B, C, D, E, F, X = map(int, input().split())

a = X // (A + C)
b = X // (D + F)
c = X % (A + C)
d = X % (D + F)
e = c // A
if e == 0:
    f = B * c
else:
    f = B * A
g = d // D
if g == 0:
    h = E * d
else:
    h = E * D

tkhs = (B * A * a) + f
aok = (E * D * b) + h

if tkhs > aok:
    print("Takahashi")
elif tkhs < aok:
    print("Aoki")
else:
    print("Draw")
