def solve(a, b, c):
    l, r = 0, 600000001
    while r - l > 1:
        mid = (l + r) // 2
        if a * mid * mid + b * mid + c <= 0:
            l = mid
        else:
            r = mid
    if a * l * l + b * l + c == 0:
        return l
    return -1


n = int(input())
d = 1
while d * d * d <= n:
    if n % d != 0:
        d += 1
        continue
    m = n // d
    k = solve(3, 3 * d, d * d - m)
    if k > 0:
        print(k + d, k)
        exit()
    d += 1
print(-1)
