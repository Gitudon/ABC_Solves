P = list(map(int, input().split()))

ans = ""
for i in P:
    ans += chr((i - 1) + ord("a"))
print(ans)
