N, M = map(int, input().split())
S = [0] * N
T = [0] * M
for i in range(N):
    S[i] = input()
ans = [0] * N


def check_distance(s, t):
    if len(s) != len(t):
        return False
    cnt = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            cnt += 1
    if cnt == 1:
        return True
    return False


for _ in range(M):
    T = input()
    cnt = 0
    idx = 0
    for i in range(N):
        if S[i] == T:
            ans[i] += 1
            cnt = 0
            break
        elif check_distance(S[i], T):
            cnt += 1
            idx = i
    if cnt == 1:
        ans[idx] += 1

for a in ans:
    print(a)
