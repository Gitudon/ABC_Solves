N, R = map(int, input().split())
L = list(map(int, input().split()))

i = 0
while i < N:
    if L[i] == 1:
        i += 1
    else:
        break

j = N - 1
while j >= 0:
    if L[j] == 1:
        j -= 1
    else:
        break


buf = L[i : j + 1]

if buf == []:
    print(0)
    exit()

ans = 0

if R - 1 > j:
    ans += 2 * (R - 1 - j)

if R - 1 < i:
    ans += 2 * (i - R)

for k in buf:
    if k == 0:
        ans += 1
    else:
        ans += 2

print(ans)
