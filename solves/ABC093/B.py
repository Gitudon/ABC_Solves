A, B, K = map(int, input().split())

ans = []
foo = 1
for i in range(A, B + 1):
    if foo <= K:
        ans.append(i)
        foo += 1

foo = 1
for i in range(B, A - 1, -1):
    if foo <= K:
        ans.append(i)
        foo += 1

ans = list(set(ans))
ans.sort()
for a in ans:
    print(a)
