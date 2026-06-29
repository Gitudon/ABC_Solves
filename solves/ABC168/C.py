A, B, H, M = map(int, input().split())

import math

ang_a = H * 30 + M * 0.5
ang_b = M * 6

rad_a = math.radians(ang_a)
rad_b = math.radians(ang_b)

x_a = A * math.cos(rad_a)
y_a = A * math.sin(rad_a)
x_b = B * math.cos(rad_b)
y_b = B * math.sin(rad_b)

print(math.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2))
