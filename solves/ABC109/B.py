N = int(input())

talked = []
ans = "Yes"
prev = input()
talked.append(prev)
for i in range(1, N):
    now = input()
    if prev[-1] != now[0] or now in talked:
        ans = "No"
    talked.append(now)
    prev = now

print(ans)
