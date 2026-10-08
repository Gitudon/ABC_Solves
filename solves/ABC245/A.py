A, B, C, D = map(int, input().split())

tkhs = A * 3600 + B * 60
aok = C * 3600 + D * 60 + 1

if tkhs < aok:
    print("Takahashi")
else:
    print("Aoki")
