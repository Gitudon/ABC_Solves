N = int(input())
ans = 0


def yakusu(n):
    ans = 0
    for i in range(1, n + 1):
        if n % i == 0:
            ans += 1
    return ans


for i in range(1, N + 1, 2):
    if yakusu(i) == 8:
        ans += 1
print(ans)
