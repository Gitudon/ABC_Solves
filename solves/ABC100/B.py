D, N = map(int, input().split())
foo = 100**D
if N == 100:
    N += 1
ans = str(N) + str(foo)[1:]
print(ans)
