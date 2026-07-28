N = int(input())
A = list(map(int, input().split()))

lim = max(A)
foo = [0] * (lim + 1)

for i in range(2, lim + 1):
    cnt = 0
    for a in A:
        if a % i == 0:
            cnt += 1
    foo[i] = cnt

ans = 0
bar = max(foo)
for i in range(len(foo)):
    if foo[i] == bar:
        ans = i
print(ans)
