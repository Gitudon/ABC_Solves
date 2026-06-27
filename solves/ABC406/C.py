N = int(input())
P = list(map(int, input().split()))
v = []
for i in range(N - 1):
    if P[i] < P[i + 1]:
        if not v or v[-1][0] == ">":
            v.append(("<", 1))
        else:
            v[-1] = (v[-1][0], v[-1][1] + 1)
    else:
        if not v or v[-1][0] == "<":
            v.append((">", 1))
        else:
            v[-1] = (v[-1][0], v[-1][1] + 1)
ans = 0
for i in range(1, len(v) - 1):
    if v[i][0] == ">":
        ans += v[i - 1][1] * v[i + 1][1]
print(ans)
