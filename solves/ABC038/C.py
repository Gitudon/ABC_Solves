N = int(input())
a = list(map(int, input().split()))

ans = N
length = 1
for i in range(1, N):
    if a[i - 1] < a[i]:
        length += 1
        ans += length - 1
    else:
        length = 1
print(ans)
