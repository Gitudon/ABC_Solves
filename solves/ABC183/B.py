Sx, Sy, Gx, Gy = map(int, input().split())

if Sy + Gy != 0:
    result = (Sx * Gy + Gx * Sy) / (Sy + Gy)
else:
    result = 0

print(result)
