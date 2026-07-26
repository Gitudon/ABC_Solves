N = int(input())


def ten_to_eight(n):
    if n == 0:
        return 0
    else:
        return n % 8 + 10 * ten_to_eight(n // 8)


ans = 0
for i in range(1, N + 1):
    if "7" not in str(ten_to_eight(i)) and "7" not in str(i):
        ans += 1
print(ans)
