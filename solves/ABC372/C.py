N, Q = map(int, input().split())
S = list(input())

ans = 0
for i in range(N - 2):
    if S[i] == "A" and S[i + 1] == "B" and S[i + 2] == "C":
        ans += 1

for _ in range(Q):
    X, C = input().split()
    X = int(X) - 1
    for k in range(3):
        idx = X - k
        if 0 <= idx <= N - 3:
            if S[idx] == "A" and S[idx + 1] == "B" and S[idx + 2] == "C":
                ans -= 1
    S[X] = C
    for k in range(3):
        idx = X - k
        if 0 <= idx <= N - 3:
            if S[idx] == "A" and S[idx + 1] == "B" and S[idx + 2] == "C":
                ans += 1
    print(ans)
