N, Q = map(int, input().split())
S = input()

now = 0
ruisekiwa = [0] * N
for i in range(1, N):
    if S[i] == S[i - 1]:
        now += 1
    ruisekiwa[i] = now

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    if l == r:
        ans = 0
    else:
        ans = ruisekiwa[r] - ruisekiwa[l]
    print(ans)
