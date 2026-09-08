N = int(input())
ans = ""
length = 0
for i in range(N):
    c, l = map(str, input().split())
    length += int(l)
    if length > 100:
        ans = "Too Long"
        print(ans)
        exit()
    ans += c * int(l)
print(ans)
