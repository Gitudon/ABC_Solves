N = int(input())
S = list(map(int, input().split()))


def honsya(a, b):
    return 4 * a * b + 3 * a + 3 * b


ans = 0
for i in range(N):
    flag = True
    for a in range(1, 1001):
        for b in range(1, 1001):
            if honsya(a, b) == S[i]:
                flag = False
                break
    if flag:
        ans += 1
print(ans)
