N = int(input())


def is_kaibun(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False


ans = 0
for i in range(1000001):
    foo = i**3
    if is_kaibun(foo):
        if foo <= N:
            ans = foo

print(ans)
