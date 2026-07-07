X, N = map(int, input().split())
p = list(map(int, input().split()))

if p == []:
    print(X)
else:
    if X not in p:
        print(X)
    else:
        ans = X
        sa = 10**9
        for i in range(-1000, 1000):
            if i not in p:
                if abs(i - X) < sa:
                    sa = abs(i - X)
                    ans = i
        print(ans)
