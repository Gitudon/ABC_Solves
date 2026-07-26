from math import gcd
from itertools import combinations_with_replacement

K = int(input())
ans = 0

for a, b, c in combinations_with_replacement(range(1, K + 1), 3):
    g = gcd(gcd(a, b), c)
    if a == b == c:
        ans += g
    elif a == b or b == c or a == c:
        ans += g * 3
    else:
        ans += g * 6

print(ans)
