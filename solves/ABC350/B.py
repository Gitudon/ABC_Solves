N, Q = map(int, input().split())
T = list(map(int, input().split()))
ha = [True] * N
for i in range(Q):
    if ha[T[i] - 1]:
        ha[T[i] - 1] = False
    else:
        ha[T[i] - 1] = True
ans = 0
for h in ha:
    if h:
        ans += 1
print(ans)
