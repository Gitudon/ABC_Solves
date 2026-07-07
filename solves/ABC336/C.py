N = int(input())


def ten_to_five(n):
    if n == 0:
        return "0"
    res = []
    while n > 0:
        res.append(str(n % 5))
        n //= 5
    return "".join(res[::-1])


res = ten_to_five(N - 1)
ans = ""
for r in res:
    if r == "0":
        ans += "0"
    elif r == "1":
        ans += "2"
    elif r == "2":
        ans += "4"
    elif r == "3":
        ans += "6"
    elif r == "4":
        ans += "8"
print(ans)
