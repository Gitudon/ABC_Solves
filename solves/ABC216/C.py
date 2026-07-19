N = int(input())

ans = ""
while N > 0:
    if N % 2 == 1:
        ans = "A" + ans
        N -= 1
    ans = "B" + ans
    N //= 2

print(ans)
