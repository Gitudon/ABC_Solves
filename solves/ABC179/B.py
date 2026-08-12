N = int(input())
ans = "No"
zorome = 0
for i in range(N):
    D1, D2 = map(int, input().split())
    if D1 == D2:
        zorome += 1
    else:
        zorome = 0
    if zorome == 3:
        ans = "Yes"
print(ans)
