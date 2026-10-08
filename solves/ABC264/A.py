L, R = map(int, input().split())
a = "atcoder"
ans = ""
for i in range(L, R + 1):
    b = a[i - 1]
    ans += b
print(ans)
